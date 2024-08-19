from django.core.cache import cache

class ChartDataRepository:

    @staticmethod
    def fetch_data():
        cache_key = 'simple_data'
        data = cache.get(cache_key)

        if not data:
            # Hardcoded data
            data = [
                {
                    "2024": [
                        {
                            "01": [
                                {"2024/01/01 , 00:00:00": 300},
                                {"2024/01/02 , 00:00:00": 400},
                                {"2024/01/03 , 00:00:00": 550},
                            ]
                        },
                        {
                            "02": [
                                {"2024/02/01 , 00:00:00": 300},
                                {"2024/02/02 , 00:00:00": 400},
                                {"2024/02/03 , 00:00:00": 550},
                            ]
                        }
                    ]
                }
            ]
            # Cache the data for future requests
            cache.set(cache_key, data, timeout=60*15)  # Cache for 15 minutes

        return data
