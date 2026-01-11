import logging
from datetime import datetime


ROOT = 'out/plots'

def save_dialog(figure, dpi=500, name=''):
    if input(f"save figure {name}?\n> Type 'Y' for yes: ").upper() == 'Y':
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        f_name = input("> enter filename: ")
        if f_name == '':
            f_name = f'figure_{name}_{f_time}.png'
        figure.savefig(
            fname=f'{ROOT}/{f_name}',
            dpi=dpi, transparent=True
        )
        logging.info(f"saved figure '{name}' as '{ROOT}/{f_name}'")
    else:
        logging.info(f"didn't save figure '{name}'")
