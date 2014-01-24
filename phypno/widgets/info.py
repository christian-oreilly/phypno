from logging import getLogger
lg = getLogger(__name__)

from datetime import timedelta
from os.path import basename
from PySide.QtGui import (QGroupBox,
                          QLabel,
                          QVBoxLayout,
                          )
from .. import Dataset


class Info(QGroupBox):    # maybe as QWidget
    """Displays information about the dataset.

    Attributes
    ----------
    parent : instance of QMainWindow
        the main window.
    filename : str
        the full path of the file.
    dataset : instance of phypno.Dataset
        the dataset already read in.

    Methods
    -------
    read_dataset : reads dataset from filename
    display_info : displays information about the dataset

    """
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.filename = None
        self.dataset = None

    def read_dataset(self, filename):
        self.filename = filename
        self.dataset = Dataset(filename)
        self.display_info()

    def display_info(self):
        header = self.dataset.header

        filename = QLabel('Filename: ' + basename(self.filename))
        filename.setToolTip('TODO: click here to open a new file')
        s_freq = QLabel('Sampl. Freq: ' + str(header['s_freq']))
        n_chan = QLabel('N. Channels: ' + str(len(header['chan_name'])))
        start_time = QLabel('Start Time: ' +
                            header['start_time'].strftime('%H:%M:%S'))
        start_time.setToolTip('Recording date is considered "Personally ' +
                              'identifiable information"')
        endtime = header['start_time'] + timedelta(seconds=header['n_samples']
                                                   / header['s_freq'])

        end_time = QLabel('End Time: ' + endtime.strftime('%H:%M:%S'))
        end_time.setToolTip('Recording date is considered "Personally ' +
                              'identifiable information"')

        vbox = QVBoxLayout()
        vbox.addWidget(filename)
        vbox.addWidget(s_freq)
        vbox.addWidget(n_chan)
        vbox.addWidget(start_time)
        vbox.addWidget(end_time)
        vbox.addStretch(1)
        self.setLayout(vbox)
