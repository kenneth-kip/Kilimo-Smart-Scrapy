# -*- coding: utf-8 -*-

# Scrapy settings for kilimo_smart project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kilimo_smart'

SPIDER_MODULES = ['kilimo_smart.spiders']
NEWSPIDER_MODULE = 'kilimo_smart.spiders'
GCS_KEY_FILE = 'ewogICAgInR5cGUiOiAic2VydmljZV9hY2NvdW50IiwKICAgICJwcm9qZWN0X2lkIjogImtpbGltby1zbWFydC02YmNlYyIsCiAgICAicHJpdmF0ZV9rZXlfaWQiOiAiNWQwOWNlMmE3YmU0OWZmNWI3ZDAyYTA2OWJkNWQwZWEwOGIwODczMyIsCiAgICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdlFJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLY3dnZ1NqQWdFQUFvSUJBUURJV0M3cjNXZGdIQUNNXG4zMXgyejJSbGlYL2RPdWVJTEV0ZFJVbk1Xczd1L2hickg3M2dtNGN0ZWxFMURTK1U0N2pUa3JnSGJib1VKaCtDXG56cnU0Q09Jd20xUDdTZU9aTjhXTHVHN3JsVW56Q3Z6dWJHVmhCRXRzdG1KaVRRdmlQYlJUb0I3cEk2eC9DcDdhXG45K2NFZ3dEOEwwTENVU2ZST2RIdVJoWnlSbm9rekR2c01xdVRSUGJSOC9iRmpGOGRMeWFxb3ZWdUlwVXBneFdMXG5vdjhGVGVkV1FzaDZVcWxFR2c5YlhOK2xKNUNObHZUR3RoRDE3Y3hTdC8vQVd0akNhazJhdFVnVkhjM2toZkZiXG5tZDlGaHU0cXNObnpXR3RPdDhmcjdoWTdWOVV4TWNqRVFTc1hiMjFYd0ZtNFpDTDdSc2N4SE1lZitDTE1nZ3dIXG5VaHQxQUZubkFnTUJBQUVDZ2dFQUJTZHZuWlhHa1F4blh6aG4wbzZuVUkxbkFyUC9QTnVXM01GcGtwNUxjSTZNXG4zR09tcU42WGJhNFY1TDJBR2Q1NTVNZURnSDFzS2hTSS92NStpYytBc2l0c3o2d285TW9naE9XcnhOZkVYVUpOXG5HMzBpWm9xTHZqSTYrYmh0czlaT2kxQTFPMTQxazljY0d4b0JrWFlsVWxlTTZoN1lYV09WYVFIWWxmd0dMR2dnXG4vd0VML0RWdnQyZkhsOWl1Rkx3YlAvZEhDYWRxcXVkSWhEV0U5YTJuMlRSdmkyRDg4STkzVTRzSnNRb3BDLzB1XG5FOCt4cG1PS0hkc25OcGdaT2ZoZnBudDk5ZkFvbzlmRTBDb0gwN2MxMzc1MEJvZ2FkODRPS1lwRHB2aEhKa0svXG5qTThudngzZmFOcHBGZHhiRXFhSDc5d2RQR0kvVUlMS1h0SDE0dkpNRVFLQmdRRHZQcXRXa3ZuK2V5Y0JJRU5iXG52YmFvNlFPdit0L2pIcEVMTEcyM3RYWlpEaHJ3TTR5cGhDelp0aGhrclhIaW1QT3N4MjhkMFNyaWFRdnI4TjB3XG5VYm5CdkQ0MUV0RnBZSXF5N2FIb0xPSStqYWRsN2dRQW0reGJGZC9yZ2VoUzNlTDM3eGcxUE9zM1JwOHBZbFJ5XG5hWkdHWXRrQVZQMTd3bnlTT3dqUWtkaVN3d0tCZ1FEV1lCV2JRMzVOaTJuUElxbVg5Y015dks3by9hc2NsYnZGXG5OZWNPVjZUcDNKeFgyVjVsak5qaFg2dUxEUDFWa0JZUHFwWDgyVVRQbGFvWHkvT0RFOU01STRlMWtCajd2eUx0XG5EZURqRjVNaWorM2FnNlBVRnFBQkY1VzZ5S0ZMUnkwaTVJcGJQWksxTW8rOG1BdEw1akRDdUdSb3hnd0NCdmY2XG42NFBMZ2tFaURRS0JnUUNYbi9FNUFoZGNlREtGSFN4emRTM1JxVFFFRVF4WnhlS0k0VlI3N0k2ZjdEZVlhaU5JXG53Qk1vdTZhRUVBU3dadDF3Y0VqMDdiNnZGWUpQdXl5RDFoZlROL2w0NjM4NnVNdk9rSnBmS2lzTkYvdXl0d0ZrXG5YVzJUWUs2MGRIV0lKMFlVZWp5dWFQaHQ1TjAwZmpRayt0RVhDWWljRkVFK2NVay82Qmd6RDJ2aHZ3S0JnRFF5XG5QdkNIOVhmQ0N5aEJBMVFacGNaenhJNjhQTzUvMHJGSTE1SlphckQ2WXlMTXJUeENtQWYvK0UrcUFRRFZUVm5SXG5LaVhmYk82eVBURUFHckYrb1Q1WFZWS3kzREpucm9SVGpiOGRYVmpiL0lqbzVubmNiR2IzckNCSGUyWk4xVUthXG5yTWxjYTUwc3kyeWJCSjBkVmlBREw0ZUhPU05CT1IzaVBEdlA0alg5QW9HQU4wQmlRZ2VESVdnZ29UN1F1YzZ5XG5POVplekRZbGxVLyszWnpqTmxORnlOeU9aQ0F6di80TXNLajUvR201K0RnbXZYeFJTQTluYU5NNHE2WEdGcjJpXG5ROEFtbFJjS3pjckZiRVpBNTFOZ2pLaVd3RGg5czkyeHl6Wjd4bmg2aDVGOGdpRTVDV2tnQ0RnWWl4a25FWUs5XG5UOHcyTFhxVWtwVlh6dmZ1ejE0T0VHWT1cbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgICAiY2xpZW50X2VtYWlsIjogImtpbGltby1zbWFydC02YmNlY0BhcHBzcG90LmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICAgImNsaWVudF9pZCI6ICIxMDQ2MzgxMTgxMjY4ODA3OTc2MDciLAogICAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAgICJ0b2tlbl91cmkiOiAiaHR0cHM6Ly9vYXV0aDIuZ29vZ2xlYXBpcy5jb20vdG9rZW4iLAogICAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkva2lsaW1vLXNtYXJ0LTZiY2VjJTQwYXBwc3BvdC5nc2VydmljZWFjY291bnQuY29tIgp9CiAg'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kilimo_smart (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'kilimo_smart.middlewares.KilimoSmartSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'kilimo_smart.middlewares.KilimoSmartDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'kilimo_smart.pipelines.KilimoSmartPipeline': 300,
   'kilimo_smart.pipelines.PricesJsonPipeline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
