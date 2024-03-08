import pygame




def hilbert_curve(index: int) -> pygame.Vector2:
    """
    Return the position of the hilbert pixel point relative to its index
    :param index: of a point
    :return: position of a point
    """
    position_list = [pygame.Vector2(0, 0), pygame.Vector2(0, 1), pygame.Vector2(1, 1), pygame.Vector2(1, 0)]
    return position_list[index]
