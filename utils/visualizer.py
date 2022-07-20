import visdom

from visdom import Visdom
import numpy as np
import argparse

DEFAULT_PORT = 8097
DEFAULT_HOSTNAME = "http://165.194.104.141"


class Visualizer():
    def __init__(self):
        parser = argparse.ArgumentParser(description='Image display arguments')
        parser.add_argument('-port', metavar='port', type=int, default=DEFAULT_PORT,
                            help='port the visdom server is running on.')
        parser.add_argument('-server', metavar='server', type=str,
                            default=DEFAULT_HOSTNAME,
                            help='Server address of the target to run the demo on.')

        FLAGS = parser.parse_args()

        self.viz = Visdom(port=FLAGS.port, server=FLAGS.server)

    def image_display(self, visuals, iter):
        idx = 1
        for label, image in visuals.items():
            self.viz.image(image.transpose([2, 0, 1]), opts=dict(title=label, width=240, height=240), win=idx, update='replace')
            idx += 1
            # if iter % 500 == 0:
            #     save_image(image_numpy, 'D:\CODE\pytorch_code\WAE_base/train_results/' + str(iter) + '_' + label + '.png')


    def plot_current_errors(self, epoch, errors):
        if not hasattr(self, 'plot_data'):
            self.plot_data = {'X':[],'Y':[], 'legend':list(errors.keys())}
        self.plot_data['X'].append(epoch)
        self.plot_data['Y'].append([errors[k] for k in self.plot_data['legend']])
        self.viz.line(
            X=np.stack([np.array(self.plot_data['X'])]*len(self.plot_data['legend']), 1),
            Y=np.array(self.plot_data['Y']),
            opts={'title': 'Training' + ' loss over time',
                'legend': self.plot_data['legend'],
                'xlabel': 'epoch',
                'ylabel': 'loss'},
            win=41, update='append')

    def plot_psnr(self, loss_step, loss_dict):
        if not hasattr(self, 'plot_data'):
            self.plot_data = {'X':[],'Y':[], 'legend':list(loss_dict.keys())}
        self.plot_data['X'].append(loss_step)
        self.plot_data['Y'].append(loss_dict)
        self.viz.line(
            X=np.array(self.plot_data['X']),
            Y=np.array(self.plot_data['Y']),
            win=50,
            opts=dict(xlabel='epoch',
                    ylabel='PSNR',
                    title='IFFI PSNR',
                    legend=self.plot_data['legend_U']),
            update='append')
