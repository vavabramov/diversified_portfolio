date_range = ('2022-04-15',  '2024-04-15')

coinmarket_base_url     = 'https://pro-api.coinmarketcap.com'
coinbase_base_url       = 'https://api.pro.coinbase.com'

latest_listings_url  = f'{coinmarket_base_url}/v1/cryptocurrency/listings/latest?sort=__sortedby__&limit=__limit__'
new_listings_url     = f'{coinmarket_base_url}/v1/cryptocurrency/listings/new?sort=__sortedby__&limit=__limit__'
historic_prices_url  = f'{coinbase_base_url}/products/__ticker__-USD/candles?start=__start_date__T12:00:00&end=__end_date__T12:00:00&granularity=86400'