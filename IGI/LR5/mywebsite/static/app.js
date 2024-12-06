class Slider {
    constructor(options) {
        this.slider = document.getElementById(options.sliderId);
        this.slides = this.slider.querySelector('.slides');
        this.slidesCount = this.slides.children.length;
        this.currentSlide = 0;
        this.loop = options.loop;
        this.navs = options.navs;
        this.pags = options.pags;
        this.auto = options.auto;
        this.delay = options.delay * 1000;
        this.stopMouseHover = options.stopMouseHover;
        this.interval = null;

        if (this.navs) {
            this.prevBtn = this.slider.querySelector('.prev');
            this.nextBtn = this.slider.querySelector('.next');
            this.prevBtn.addEventListener('click', () => this.prevSlide());
            this.nextBtn.addEventListener('click', () => this.nextSlide());
        }

        if (this.pags) {
            this.pagination = this.slider.querySelector('.slide-pagination');
            this.paginationSpans = this.pagination.querySelectorAll('span');
            this.paginationSpans.forEach(span => {
                span.addEventListener('click', (e) => this.goToSlide(parseInt(e.target.getAttribute('data-index'))));
            });
        }

        if (this.auto) {
            this.startAutoSlide();
            if (this.stopMouseHover) {
                this.slider.addEventListener('mouseover', () => this.stopAutoSlide());
                this.slider.addEventListener('mouseout', () => this.auto ? this.startAutoSlide() : "");
            }
        }
    }

    updateSettings(options) {
        this.loop = options.loop;
        this.navs = options.navs;
        this.pags = options.pags;
        this.auto = options.auto;
        this.delay = options.delay * 1000;
        this.stopMouseHover = options.stopMouseHover;

        if (this.auto) {
            this.startAutoSlide();
        } else {
            this.stopAutoSlide();
        }

        if (this.pags) {
            this.showPags();
        }
        else {
            this.hidePags();
        }

        if (this.navs) {
            this.showNavs();
        }
        else {
            this.hideNavs();
        }

        this.updateSlider();
    }

    startAutoSlide() {
        this.stopAutoSlide();
        this.interval = setInterval(() => this.nextSlide(), this.delay);
    }

    stopAutoSlide() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }

    goToSlide(index) {
        this.currentSlide = index;
        this.updateSlider();
    }

    prevSlide() {
        this.currentSlide = this.currentSlide === 0 ? (this.loop ? this.slidesCount - 1 : 0) : this.currentSlide - 1;
        this.updateSlider();
    }

    nextSlide() {
        this.currentSlide = this.currentSlide === this.slidesCount - 1 ? (this.loop ? 0 : this.slidesCount - 1) : this.currentSlide + 1;
        this.updateSlider();
    }

    updateSlider() {
        this.slides.style.transform = `translateX(-${this.currentSlide * 100}%)`;
        if (this.pags) {
            this.paginationSpans.forEach(span => span.classList.remove('active'));
            this.paginationSpans[this.currentSlide].classList.add('active');
        }
    }

    hideNavs() {
        var leftPag = this.slider.querySelector('.prev');
        leftPag.hidden = true;
        var rightPag = this.slider.querySelector('.next');
        rightPag.hidden = true;
    }

    showNavs() {
        var leftPag = this.slider.querySelector('.prev');
        leftPag.hidden = false;
        var rightPag = this.slider.querySelector('.next');
        rightPag.hidden = false;
    }

    showPags() {
        let pags = this.slider.querySelectorAll('.pagination span');
        for (let index = 0; index < pags.length; index++) {
            pags[index].hidden = false;
        }
    }

    hidePags() {
        let pags = this.slider.querySelectorAll('.pagination span');
        for (let index = 0; index < pags.length; index++) {
            pags[index].hidden = true;
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {

    // СЛАЙДЕР
    const slider = new Slider({
        sliderId: 'slider',
        loop: true,
        navs: true,
        pags: true,
        auto: true,
        delay: 5,
        stopMouseHover: true
    });

    document.getElementById('updateSettings').addEventListener('click', () => {
        const delay = document.getElementById('delay').value;
        const loop = document.getElementById('loop').checked;
        const navs = document.getElementById('navs').checked;
        const pags = document.getElementById('pags').checked;
        const auto = document.getElementById('auto').checked;

        slider.updateSettings({
            loop: loop,
            navs: navs,
            pags: pags,
            auto: auto,
            delay: delay,
            stopMouseHover: true
        });

        console.log("Updated settings:", {
            loop: loop,
            navs: navs,
            pags: pags,
            auto: auto,
            delay: delay,
            stopMouseHover: true
        });
    });

    // ТАЙМЕР
    const countdownElement = document.getElementById('countdown');
    countdownElement.innerHTML = 'Таймер: ';
    const countdownDuration = 60 * 60 * 1000;
    const now = new Date().getTime();
    let endTime = localStorage.getItem('countdownEndTime');

    if (!endTime) {
        endTime = now + countdownDuration;
        localStorage.setItem('countdownEndTime', endTime);
    }

    function updateCountdown() {
        const now = new Date().getTime();
        const distance = endTime - now;

        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownElement.innerHTML = 'Таймер: ' + hours + "ч " + minutes + "м " + seconds + "с ";

        if (distance < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = "Обратный отсчет завершен!";
            localStorage.removeItem('countdownEndTime');
        }
    }

    const countdownInterval = setInterval(updateCountdown, 1000);

    // ПАГИНАЦИЯ
    const services = [
        { id: 1, name: "Удаление прыщей", price: "1000₽" },
        { id: 2, name: "Коррекция глаза", price: "2000₽" },
        { id: 3, name: "Консультация", price: "3000₽" },
        { id: 4, name: "Удаление акне", price: "4000₽" },
        { id: 5, name: "Прокол ушей", price: "5000₽" },
        { id: 6, name: "Лечение гипергидроза", price: "6000₽" },
        { id: 7, name: "Микротоковая терапия", price: "7000₽" },
        { id: 8, name: "Мужская косметология", price: "8000₽" },
        { id: 9, name: "Чистка лица", price: "9000₽" },
        { id: 10, name: "Паралифтинг", price: "9999₽" }
    ];

    const itemsPerPage = 3;
    let currentPage = 1;

    const servicesGrid = document.getElementById('services-grid');
    const pagination = document.getElementById('pagination');
    const prevPageButton = document.getElementById('prevPage');
    const nextPageButton = document.getElementById('nextPage');
    const pageInfo = document.getElementById('pageInfo');

    function displayServices(page) {
        servicesGrid.innerHTML = '';
        const start = (page - 1) * itemsPerPage;
        const end = start + itemsPerPage;
        const pageServices = services.slice(start, end);

        pageServices.forEach(service => {
            servicesGrid.innerHTML += `
                <div class="card-wrapper"> 
                <div class="card">
                 <div class="grid-item">${service.name}</div> 
                 <div class="grid-item">${service.price}</div> 
                 <div class="grid-item" id="view"><a href="services/view/${service.id}">Просмотр</a></div> 
                </div> 
                </div>
            `;
        });

        updatePageInfo();
        addCardEffects();
    }

    function setupPagination() {
        const pageCount = Math.ceil(services.length / itemsPerPage);
        updatePageButtons();
        updatePageInfo();
    }

    function updatePageButtons() {
        const pageCount = Math.ceil(services.length / itemsPerPage);
        prevPageButton.disabled = currentPage === 1;
        nextPageButton.disabled = currentPage === pageCount;
    }

    function updatePageInfo() {
        const pageCount = Math.ceil(services.length / itemsPerPage);
        pageInfo.innerText = `Страница ${currentPage} из ${pageCount}`;
    }

    function addCardEffects() {
        const cards = document.querySelectorAll(".card-wrapper");
        cards.forEach(card_w => {
            const card = card_w.querySelector(".card");
            card_w.addEventListener('mousemove', event => {
                const [x, y] = [event.offsetX, event.offsetY];
                const rect = card_w.getBoundingClientRect();
                const [width, height] = [rect.width, rect.height];
                const middleX = width / 2;
                const middleY = height / 2;
                const offsetX = ((x - middleX) / middleX) * 25;
                const offsetY = ((y - middleY) / middleY) * 25;
                const offX = 50 + ((x - middleX) / middleX) * 25;
                const offY = 50 - ((y - middleY) / middleY) * 20;
                card.style.setProperty("--rotateX", 1 * offsetX + "deg");
                card.style.setProperty("--rotateY", -1 * offsetY + "deg");
                card.style.setProperty("--posx", offX + "%");
                card.style.setProperty("--posy", offY + "%");
            });

            card_w.addEventListener('mouseleave', eve => {
                card.style.animation = 'reset-card 1s ease';
                card.addEventListener("animationend", e => {
                    card.style.animation = 'unset';
                    card.style.setProperty("--rotateX", "0deg");
                    card.style.setProperty("--rotateY", "0deg");
                    card.style.setProperty("--posx", "50%");
                    card.style.setProperty("--posy", "50%");
                },
                    {
                        once: true
                    });
            });
        });

    }

    prevPageButton.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            displayServices(currentPage);
            updatePageButtons();
        }
    });

    nextPageButton.addEventListener('click', () => {
        const pageCount = Math.ceil(services.length / itemsPerPage);
        if (currentPage < pageCount) {
            currentPage++;
            displayServices(currentPage);
            updatePageButtons();
        }
    });

    displayServices(currentPage);
    setupPagination();


    // Дата рождения
    function calculateAge(birthDate) {
        const today = new Date();
        const birth = new Date(birthDate);
        let age = today.getFullYear() - birth.getFullYear();
        const monthDiff = today.getMonth() - birth.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
            age--;
        }
        return age;
    }

    function getDayOfWeek(date) {
        const days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
        const day = new Date(date).getDay();
        return days[day];
    }

    function checkAge() {
        const birthDate = prompt("Введите вашу дату рождения (в формате ГГГГ-ММ-ДД):");
        if (!birthDate) {
            alert("Дата рождения не введена");
            return;
        }

        const age = calculateAge(birthDate);

        if (age < 18) {
            alert("Вы несовершеннолетний. Необходимо разрешение родителей для использования сайта.");
        } else {
            const dayOfWeek = getDayOfWeek(birthDate);
            alert(`Вы совершеннолетний. День недели вашей даты рождения: ${dayOfWeek}.`);
        }
    }

    checkAge();

    // СКРОЛЛИНГ

    const molecules = document.querySelectorAll('.molecule');
    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;
        const maxScroll = document.body.scrollHeight - window.innerHeight;
        const scrollFraction = scrollPosition / maxScroll;
        molecules.forEach((molecule, index) => {
            const scale = 2 - scrollFraction;
            const rotate = scrollFraction * 360;
            const opacity = 1 - scrollFraction;
            if (index === 0) {
                molecule.style.transform = `translateX(${scrollFraction * 100}px) scale(${scale}) rotate(${rotate}deg)`;
            } else if (index === 1) {
                molecule.style.transform = `translateX(-${scrollFraction * 100}px) scale(${scale}) rotate(${rotate}deg)`;
            } molecule.style.opacity = opacity;
        });
    });

    // АНИМАЦИИ
    let circle = document.getElementById('animationCircle');

    const frames = [{
        transform: "translateX(10%)",
    }, {
        transform: "translateX(50%)",
    }, {
        transform: "translateX(90%)",
    }];

    const config = {
        duration: 3000,            
        easing: "ease-in-out",  
        delay: 200,              
        iterations: Infinity,   
        direction: "alternate",  
        fill: "both"            
    };

    circle.addEventListener('click', () => {
        circle.animate(frames, config);
    });

    // API
    const locationDiv = document.getElementById('location');

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const latitude = position.coords.latitude.toFixed(2);
                const longitude = position.coords.longitude.toFixed(2);
                locationDiv.innerHTML = `Ваше текущее местоположение: широта ${latitude}, долгота ${longitude}`;
            },
            error => {
                locationDiv.innerHTML = 'Невозможно определить местоположение.';
            }
        );
    } else {
        locationDiv.innerHTML = 'Геолокация не поддерживается вашим браузером.';
    }

    navigator.getBattery()
        .then((battery) => displayBattery(battery));

    function displayBattery(battery) {
        const batteryDiv = document.getElementById('battery');
        let batteryLevel = battery.level * 100 + "%";
        batteryDiv.innerHTML = `Текущий уровень заряда: ${batteryLevel}, `
        if (battery.charging) {
            batteryDiv.innerHTML += 'Заряжается';
        } else {
            batteryDiv.innerHTML += 'Не заряжается';
        }
    }
});


