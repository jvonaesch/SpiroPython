import logging
import types

from spiro.EvaluationRecord import EvaluationRecord


class Evaluator:

    def __init__(self, func, args, name='eval'):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self, record: EvaluationRecord):
        vals = record[self]
        if vals is None:
            eval_args = []
            for arg in self.args:
                if isinstance(arg, Evaluator):
                    logging.info(f"{self} requested input from {arg}")
                    eval_args.append(arg(record))
                elif isinstance(arg, types.LambdaType):
                    logging.info(f"{self} generated input using lambda expression {arg}")
                    eval_args.append(arg(record.x))
                elif arg == 't':
                    logging.info(f"{self} used time as an input")
                    eval_args.append(record.x)
                else:
                    logging.info(f"{self} received numerical input")
                    eval_args.append(arg)
            record[self] = self.func(*eval_args)
            logging.info(f"{self} finished generating output")
        else:
            logging.info(f"{self} returned pre-generated output")
        return record[self]

    def __str__(self):
        return f"evaluator '{self.name}'"