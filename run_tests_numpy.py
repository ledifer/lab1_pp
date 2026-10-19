from grader_contracts.numpy_tasks import *
from numpy_tasks import *

if __name__ == '__main__':
    print("Задача 1.")
    matrices = [np.array([[1, 2], [3, 4]]), np.array([[0, 1], [1, 0]])]
    vectors = [np.array([[1], [1]]), np.array([[2], [3]])]
    print(sum_prod(MatrixVectorBatchInput(matrices, vectors)))

    print("\nЗадача 2.")
    matrix_2 = np.array([[0.1, 0.6], [0.8, 0.4]])
    print(binarize(BinarizeInput(matrix_2, 0.5)))

    print("\nЗадача 3.")
    matrix_3 = np.array([[1, 2, 1, 3], [4, 4, 4, 4], [5, 6, 5, 7]])
    print("Уникальные в строках:", unique_rows(MatrixInput(matrix_3)))
    print("Уникальные в столбцах:", unique_columns(MatrixInput(matrix_3)))

    print("\nЗадача 4.")
    stat_res = matrix_statistics(RandomMatrixInput(3, 4, 0.0, 1.0, 42))
    print("Матрица:\n", np.round(stat_res.matrix, 2))
    print("Средние по строкам:", np.round(stat_res.row_means, 2))
    print("Средние по столбцам:", np.round(stat_res.column_means, 2))
    print("Дисперсия по строкам:", np.round(stat_res.row_variances, 2))
    print("Дисперсия по столбцам:", np.round(stat_res.column_variances, 2))

    print("\nЗадача 5.")
    print(chess(ChessInput(3, 4, 0, 1)))

    print("\nЗадача 6.")
    rect = draw_rectangle(RectangleInput(2, 3, 5, 5, (255, 0, 0), (0, 0, 0)))
    print("Форма матрицы прямоугольника:", rect.shape)
    ellipse = draw_ellipse(EllipseInput(2, 3, 7, 7, (0, 255, 0), (0, 0, 255)))
    print("Форма матрицы эллипса:", ellipse.shape)

    print("\nЗадача 7.")
    ts_res = analyze_time_series(TimeSeriesInput([1, 5, 2, 4, 3], 3))
    print(f"Среднее: {ts_res.mean}")
    print(f"Дисперсия: {ts_res.variance}")
    print(f"СКО: {ts_res.std}")
    print(f"Индексы локальных максимумов: {ts_res.local_maxima_indices}")
    print(f"Индексы локальных минимумов: {ts_res.local_minima_indices}")
    print(f"Скользящее среднее: {ts_res.moving_average}")

    print("\nЗадача 8.")
    labels = [0, 2, 3, 0]
    print("Без указания class_count")
    print(one_hot(OneHotInput(labels)))
    print("\nС указанием class_count=5")
    print(one_hot(OneHotInput(labels, 5)))