document.addEventListener('DOMContentLoaded', function () {
    const toggleSettings = document.getElementById('toggleSettings');
    const settingsPanel = document.getElementById('settingsPanel');
    const fontSizeInput = document.getElementById('fontSize');
    const textColorInput = document.getElementById('textColor');
    const bgColorInput = document.getElementById('bgColor');
    const content = document.querySelector('.content');

    toggleSettings.addEventListener('change', function () {
        if (toggleSettings.checked) {
            settingsPanel.style.display = 'block';
        } else {
            settingsPanel.style.display = 'none';
        }
    });

    fontSizeInput.addEventListener('input', function () {
        content.style.fontSize = fontSizeInput.value + 'px';
    });

    textColorInput.addEventListener('input', function () {
        content.style.color = textColorInput.value;
    });

    bgColorInput.addEventListener('input', function () {
        document.body.style.backgroundColor = bgColorInput.value;
    });


    // ГРАФИК ФУНКЦИИ

    const ctx = document.getElementById('myChart').getContext('2d');
    const xNum = 100;
    const xValues = new Array(xNum);
    let startValue = -1;
    let endValue = 1;
    let step = (endValue - startValue) / xNum;
    for (let i = 0; i < xValues.length; i++) {
        xValues[i] = startValue;
        startValue += step;
    }

    const n = 20;

    function taylorArcsin(x, n) {
        let sum = 0;
        for (let k = 0; k <= n; k++) {
            const term = (fact(2 * k) / (Math.pow(4, k) * Math.pow(fact(k), 2) * (2 * k + 1))) * Math.pow(x, 2 * k + 1);
            sum += term;
        }
        return sum;
    }

    function fact(n) {
        if (n == 0)
            return 1;
        return n * fact(n - 1);
    }

    const taylorValues = xValues.map(x => taylorArcsin(x, n));
    const exactValues = xValues.map(x => Math.asin(x));

    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Разложение в ряд Тейлора',
                    data: [],
                    borderColor: 'blue',
                    fill: false,
                    borderWidth: 1,
                    radius: 1
                },
                {
                    label: 'arcsin(x)',
                    data: [],
                    borderColor: 'red',
                    fill: false,
                    borderWidth: 1,
                    radius: 1
                }
            ]
        },
        options: {
            animation: {
                duration: 0
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'x'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'F(x)'
                    },
                    suggestedMin: -2,
                    suggestedMax: 1.5
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                title: {
                    display: true,
                    text: 'График функции'
                },
                annotation: {
                    annotations: {
                        line1: {
                            type: 'line',
                            yMin: 0,
                            yMax: 0,
                            borderColor: 'black',
                            borderWidth: 1,
                            label: {
                                content: 'Ось x',
                                enabled: true,
                                position: 'end'
                            }
                        },
                        line2: {
                            type: 'line',
                            xMin: 0,
                            xMax: 0,
                            borderColor: 'black',
                            borderWidth: 1,
                            label: {
                                content: 'Ось y',
                                enabled: true,
                                position: 'end'
                            }
                        }
                    }
                }
            }
        }
    });

    let currentIndex = 0;

    (function addDataPoints() {
        if (currentIndex < xValues.length) {
            myChart.data.labels.push(xValues[currentIndex]);
            myChart.data.datasets[0].data.push(taylorValues[currentIndex]);
            myChart.data.datasets[1].data.push(exactValues[currentIndex]);
            myChart.update();
            currentIndex++;
            requestAnimationFrame(addDataPoints);
        }
    })();


    // РЕШЕНИЕ ЗАДАЧИ 

    // Прототипное наследование
    function Book(subject, author) {
        this.subject = subject;
        this.author = author;
    }

    Book.prototype.getSubject = function () {
        return this.subject;
    };

    Book.prototype.getAuthor = function () {
        return this.author;
    };

    Book.prototype.setSubject = function (subject) {
        this.subject = subject;
    };

    Book.prototype.setAuthor = function (author) {
        this.author = author;
    };

    function SchoolBook(subject, author, classNumber) {
        Book.call(this, subject, author);
        this.classNumber = classNumber;
    }

    SchoolBook.prototype = Object.create(Book.prototype);
    SchoolBook.prototype.constructor = SchoolBook;

    SchoolBook.prototype.getClassNumber = function () {
        return this.classNumber;
    };

    SchoolBook.prototype.setClassNumber = function (classNumber) {
        this.classNumber = classNumber;
    };

    SchoolBook.prototype.display = function () {
        return `${this.subject} - ${this.author} (Класс ${this.classNumber})`;
    };

    // ООП
    class BookClass {
        constructor(subject, author) {
            this.subject = subject;
            this.author = author;
        }

        getSubject() {
            return this.subject;
        }

        getAuthor() {
            return this.author;
        }

        setSubject(subject) {
            this.subject = subject;
        }

        setAuthor(author) {
            this.author = author;
        }
    }

    class SchoolBookClass extends BookClass {
        constructor(subject, author, classNumber) {
            super(subject, author);
            this.classNumber = classNumber;
        }

        getClassNumber() {
            return this.classNumber;
        }

        setClassNumber(classNumber) {
            this.classNumber = classNumber;
        }

        display() {
            return `${this.subject} - ${this.author} (Класс ${this.classNumber})`;
        }
    }

    const textbooks = [];

    function addTextbook() {
        const subject = document.getElementById('subject').value;
        const author = document.getElementById('author').value;
        const classNumber = document.getElementById('classNumber').value;

        const useOOP = document.getElementById('useOOP').checked;
        let textbook;
        if (useOOP) {
            textbook = new SchoolBookClass(subject, author, classNumber);
        } else {
            textbook = new SchoolBook(subject, author, classNumber);
        }

        textbooks.push(textbook);
        displayTextbooks();
    }

    function displayTextbooks() {
        const list = document.getElementById('textbookList');
        list.innerHTML = '';
        textbooks.forEach((textbook) => {
            const item = document.createElement('div');
            item.innerText = textbook.display();
            list.appendChild(item);
        });
    }

    function findMostFrequentSubject() {
        const classNumber = prompt("Введите номер класса для анализа:");
        const classBooks = textbooks.filter(book => book.getClassNumber() == classNumber);
        const subjectCount = {};
        classBooks.forEach(book => {
            if (!subjectCount[book.getSubject()]) {
                subjectCount[book.getSubject()] = new Set();
            }
            subjectCount[book.getSubject()].add(book.getAuthor());
        });
        let maxCount = 0;
        let mostFrequentSubject = '';
        for (let subject in subjectCount) {
            if (subjectCount[subject].size > maxCount) {
                maxCount = subjectCount[subject].size;
                mostFrequentSubject = subject;
            }
        }
        const result = document.getElementById('result');
        result.innerHTML = `Больше всего учебников различных авторов по предмету "${mostFrequentSubject}" для класса ${classNumber}`;
    }

    document.getElementById('addTextbookButton').addEventListener('click', () => addTextbook());
    document.getElementById('resultButton').addEventListener('click', () => findMostFrequentSubject());


});