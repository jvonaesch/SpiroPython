import logging
import numpy as np
import types

from spiro.EvaluationRecord import EvaluationRecord


class EvaluationNode:

    def __init__(self, func, args, name='eval'):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self, x):
        return self.evaluate(x)

    def evaluate(self, x):
        if isinstance(x, EvaluationRecord):
            return self.record_evaluate(x)
        elif isinstance(x, int):
            x = np.linspace(0, 1, x)
        record = EvaluationRecord(x)
        return self.record_evaluate(record)

    def record_evaluate(self, record: EvaluationRecord):
        vals = record[self]
        if vals is None:
            eval_args = []
            for arg in self.args:
                if isinstance(arg, EvaluationNode):
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
        return f"node '{self.name}'"