from PowerSeries import PowerSeries as ps

def main(string:str):
    power_series = ps(0.001)

    power_series.draw_graphs("Task 3/graph.png")

    mean, med, mod, var, std_dev = power_series.compute_statistics()

    print(f"Mean: {mean}")
    print(f"Median: {med}")
    print(f"Mode: {mod}")
    print(f"Variance: {var}")
    print(f"Standard Deviation: {std_dev}")

#студент лох объелся блох )))))))))))))))))))))))))))))))))))))))))))))))

if __name__ == "__main__":
    main()
