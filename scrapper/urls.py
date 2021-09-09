from django.urls import path
from . import views


urlpatterns = [
    # main pages
	path('', views.home, name='home'),
	path('amazon_scrapper/', views.amazonScrapper, name='amazon_scrapper'),
	path('noon_scrapper/', views.noonScrapper, name='noon_scrapper'),
	path('search_titles', views.searchTitles, name='search_titles'),
    path('amazon_product_variations/', views.productVaraitions, name='productVaraitions'),
    path('amazon_product_total_variations/', views.productTotalVariations, name='productTotalVariations'),
	path('stats/', views.dataStats, name='stats'),

    # Cartlow Manager
	path('robust_search_valid/', views.robustSearchValid, name='robust_search_valid'),
	path('robust_search_details/', views.robustSearchDetails, name='robust_search_details'),

    path('save_variations/', views.saveVariations, name='save_variations'),
    path('varience_crawler/', views.varienceCrawler, name='varience_crawler'),
    path('total_varience/', views.productTotalVarience, name='total_varience'),

    path('export_csv/', views.export_csv, name='export_csv'),
	path('export_demanded_json/', views.export_demanded_json, name='export_demanded_json'),
    path('requiredJsonFormat/', views.requiredJsonFormat, name='requiredJsonFormat'),

	path('robust_search_valid_ksa/', views.robustSearchValidKSA, name='robust_search_valid_ksa'),
	path('export_csv_ksa/', views.export_csv_ksa, name='export_csv_ksa'),

    # Category work
    path('view_categories/', views.viewCategories, name='view_categories'),
    path('category_details/<str:pk>/', views.viewCategoryAttributes, name='category_details'),

    path('category_job/', views.categoryJob, name='category_job'),

    path('category_exported/<str:cid>/', views.categoryRequiredExportJson, name='category_exported'),
    path('category_export_ar_json', views.categoryExportARJson, name='category_export_ar_json'),
    path('category_export_json', views.categoryExportJson, name='category_export_json'),
    path('category_export', views.categoryExportJsonBoth, name='category_export'),

    # View Products
    path('view_products/', views.viewProducts, name='view_products'),
    path('product_details/<str:pk>/', views.amazonProductDetails, name='product_details'),
    path('product_arabic_details/<str:pk>/', views.productDetailsArabic, name='product_arabic_details'),

    path('single_product/', views.singleProductValidate, name='single_product'),
    path('asin_delete/', views.deleteAsin, name='delete_asin'),

    path('sample_json', views.sampleJson, name='sample_json'),
]