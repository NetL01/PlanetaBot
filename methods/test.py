import requests

def get_quickchart_plot(func_string):
    url = f'https://quickchart.io/chart?c={{type:\'line\',data:{{labels:[],datasets:[{{label:\'Function\',data:['']}}]}}}}'

    response = requests.get(url)

    # Получаем ссылку на изображение графика
    plot_url = response.url

    # Скачиваем изображение
    image_response = requests.get(plot_url)
    with open('plot.png', 'wb') as f:
        f.write(image_response.content)

if __name__ == "__main__":
    func_string = input("Введите функцию: ")
    get_quickchart_plot(func_string)