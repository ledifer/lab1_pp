"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    result = np.zeros_like(vectors[0])
    for A, x in zip(matrices, vectors):
        result += A @ x 
        
    return result


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    return (matrix > threshold).astype(int)


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(row).tolist() for row in matrix]


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(col).tolist() for col in matrix.T]


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    np.random.seed(seed)
    matrix = np.random.normal(loc=mean, scale=std, size=(rows, columns))
    
    row_means = np.mean(matrix, axis=1)
    column_means = np.mean(matrix, axis=0)
    
    row_variances = np.var(matrix, axis=1)
    column_variances = np.var(matrix, axis=0)
    
    return MatrixStatistics(
        matrix=matrix,
        row_means=row_means,
        column_means=column_means,
        row_variances=row_variances,
        column_variances=column_variances
    )


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    checkerboard_mask = (np.indices((rows, columns)).sum(axis=0) % 2 == 0)
    
    return np.where(checkerboard_mask, first, second)


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    canvas = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    
    cx = image_width // 2
    cy = image_height // 2
    
    start_y = max(0, cy - height // 2)
    end_y = min(image_height, start_y + height)
    
    start_x = max(0, cx - width // 2)
    end_x = min(image_width, start_x + width)
    canvas[start_y:end_y, start_x:end_x] = shape_color
    
    return canvas


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    canvas = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    
    cx = image_width // 2
    cy = image_height // 2
    
    y, x = np.ogrid[:image_height, :image_width]
    
    mask = ((x - cx)**2 / semi_axis_x**2) + ((y - cy)**2 / semi_axis_y**2) <= 1
    canvas[mask] = shape_color
    
    return canvas


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    values = np.asarray(values, dtype=float)
    
    mean = np.mean(values)
    variance = np.var(values)
    std_val = np.std(values)
    
    left = values[:-2]      
    center = values[1:-1]   
    right = values[2:]      
    
    maxima = np.where((center > left) & (center > right))[0] + 1
    minima = np.where((center < left) & (center < right))[0] + 1
    
    kernel = np.ones(window) / window
    moving_average = np.convolve(values, kernel, mode='valid')
    
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std_val,
        local_maxima_indices=maxima,
        local_minima_indices=minima,
        moving_average=moving_average
    )


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    labels = np.asarray(labels, dtype=int)
    if class_count is None:
        if len(labels) == 0:
            return np.zeros((0, 0), dtype=int)
        n_classes = np.max(labels) + 1
    else:
        n_classes = class_count
        
    result = np.zeros((len(labels), n_classes), dtype=int)
    result[np.arange(len(labels)), labels] = 1
    
    return result
