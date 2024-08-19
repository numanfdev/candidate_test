from .repositories import ChartDataRepository

class ChartDataService:
    @staticmethod
    def get_simple_data():
        return ChartDataRepository.fetch_data()
