train_count=50 # number of audios per number to train
val_count=50 # to validate
test_count=50 # to test

mel_win = 25 # millisec
mel_step = 10
mel_channel = 40
num_frames = 101

num_classes = 10
model_hidden_size = 256
model_layers = 3
method = "mean"

num_epoch =  50
lr = 3e-3
batch_size = 32
num_workers = 4