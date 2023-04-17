from rest_framework import pagination


class ProductPaginator(pagination.PageNumberPagination):
    page_size = 20

class BrandPaginator(pagination.PageNumberPagination):
    page_size = 5

class EvaluatePaginator(pagination.PageNumberPagination):
    page_size = 5