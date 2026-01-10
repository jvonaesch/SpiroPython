from datetime import datetime


ROOT = 'out/plots'

def save_dialog(figure, dpi=500):
    if input("save image?\n> Type 'Y' for yes and 'N' for no: ").upper() == 'Y':
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        f_name = input("> enter filename: ")
        if f_name == '':
            f_name = f'figure_{f_time}.png'
        figure.savefig(
            fname=f'{ROOT}/{f_name}',
            dpi=dpi, transparent=True
        )