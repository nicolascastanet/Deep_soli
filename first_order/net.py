import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
#from torch.optim import *

class CNNModel_1(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel_1, self).__init__()
        
        self.conv_layer1 = nn.Sequential(
                            nn.Conv3d(4, 32, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer2 = self._conv_layer_set(32, 64)
        self.fc1 = nn.Linear(225792, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self.batch=nn.BatchNorm1d(128)
        # Dropout
        self.drop=nn.Dropout(p=0.2)

    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
        nn.Conv3d(in_c, out_c, kernel_size=(3, 3, 3), padding=0),
        nn.ReLU(),
        nn.MaxPool3d((2, 2, 2)),
        )
        return conv_layer

    def forward(self, x):
        x = self.conv_layer1(x)
        x = self.conv_layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc2(x)
        return x


class CNNModel_2(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel_2, self).__init__()
        
        self.conv_layer1 = nn.Sequential(
                            nn.Conv3d(4, 32, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer2 = self._conv_layer_set(32, 64)
        self.fc1 = nn.Linear(225792, 128)
        self.fc2 = nn.Linear(128,128)
        self.fc3 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self.batch=nn.BatchNorm1d(128)
        # Dropout
        self.drop=nn.Dropout(p=0.5)
        
    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
        nn.Conv3d(in_c, out_c, kernel_size=(3, 3, 3), padding=0),
        nn.ReLU(),
        nn.MaxPool3d((2, 2, 2)),
        )
        return conv_layer
    

    def forward(self, x):
        x = self.conv_layer1(x)
        x = self.conv_layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc3(x)
        
        return x


class CNNModel_4(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel_4, self).__init__()
        
        self.conv_layer1 = nn.Sequential(
                            nn.Conv3d(4, 32, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer2 = nn.Sequential(
                            nn.Conv3d(32, 64, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())

        self.conv_layer3 = nn.Sequential(
                            nn.Conv3d(64, 128, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())

        self.conv_layer4 = nn.Sequential(
                            nn.Conv3d(128, 256, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer5 = self._conv_layer_set(256, 512)
        self.fc1 = nn.Linear(367744, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, num_classes)
        self.relu = nn.ReLU()
        self.batch=nn.BatchNorm1d(128)
        # Dropout
        self.drop=nn.Dropout(p=0.5)
        
    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
        nn.Conv3d(in_c, out_c, kernel_size=(3, 3, 3), padding=0),
        nn.ReLU(),
        nn.MaxPool3d((2, 2, 2)),
        )
        return conv_layer
    

    def forward(self, x):
        x = self.conv_layer1(x)
        x = self.conv_layer2(x)
        x = self.conv_layer3(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc2(x)
        return x        


class CNNModel_3(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel_3, self).__init__()
        
        self.conv_layer1 = nn.Sequential(
                            nn.Conv3d(4, 32, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer2 = nn.Sequential(
                            nn.Conv3d(32, 64, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer3 = self._conv_layer_set(64, 128)
        self.fc1 = nn.Linear(367744, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self.batch=nn.BatchNorm1d(128)
        # Dropout
        self.drop=nn.Dropout(p=0.5)
        
    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
        nn.Conv3d(in_c, out_c, kernel_size=(3, 3, 3), padding=0),
        nn.ReLU(),
        nn.MaxPool3d((2, 2, 2)),
        )
        return conv_layer
    

    def forward(self, x):
        x = self.conv_layer1(x)
        x = self.conv_layer2(x)
        x = self.conv_layer3(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc2(x)
        return x        


class CNN_RNN_model(nn.Module):
    def __init__(self, num_classes):
        super(CNN_RNN_model, self).__init__()
    
        self.conv_layer1 = nn.Sequential(
                            nn.Conv3d(4, 32, kernel_size=(3, 3, 3), padding=0),
                            nn.ReLU())
        
        self.conv_layer2 = self._conv_layer_set(32, 64)
        self.fc1 = nn.Linear(225792, 128)
        self.fc2 = nn.Linear(128,128)
        self.fc3 = nn.Linear(12800,num_classes)
        self.relu = nn.ReLU()
        self.batch=nn.BatchNorm1d(128)
        # Dropout
        self.drop=nn.Dropout(p=0.2)
        self.rnn=nn.LSTM(1, 100, dropout = 0.5, batch_first=True)
        
    def _conv_layer_set(self, in_c, out_c):
        conv_layer = nn.Sequential(
        nn.Conv3d(in_c, out_c, kernel_size=(3, 3, 3), padding=0),
        nn.ReLU(),
        nn.MaxPool3d((2, 2, 2)),
        )
        return conv_layer
    

    def forward(self, x):
        x = self.conv_layer1(x)
        x = self.conv_layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.batch(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = x.view(x.size(0),128,1)
        out, (hn, cn) = self.rnn(x)
        x = out.contiguous().view(out.size(0), -1)
        x = self.fc3(x)
    
        return x
