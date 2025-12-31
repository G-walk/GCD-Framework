class Param():
    
    def __init__(self, args):
        
        self.hyper_param = self.get_hyper_parameters(args)

    def get_hyper_parameters(self, args):
        """
        Args:
            bert_model (directory): The path for the pre-trained bert model.
            max_seq_length (autofill): The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded.
            num_train_epochs (int): The number of training epochs.
            num_pretrain_epochs (int): The number of pre-training epochs.
            num_labels (autofill): The output dimension.
            freeze_bert_parameters (binary): Whether to freeze all parameters but the last layer.
            feat_dim (int): The feature dimension.
            warmup_proportion (float): The warmup ratio for learning rate.
            lr_pre (float): The learning rate for pre-training the backbone.
            lr (float): The learning rate for training the backbone.
            loss_fct (str): The loss function for training.
            activation (str): The activation function of the hidden layer (support 'relu' and 'tanh').
            train_batch_size (int): The batch size for training.
            eval_batch_size (int): The batch size for evaluation.
            test_batch_size (int): The batch size for testing. 
            wait_patient (int): Patient steps for Early Stop.
        """
        hyper_parameters = {
            'save_results_path' : 'outputs',
            'pretrain_dir': 'pretrain_models',
            'train_dir' : 'train_models' ,
            'bert_model' : 'uncased_L-12_H-768_A-12',
            'tokenizer' : 'uncased_L-12_H-768_A-12',
            'pretrained_bert_model' : 'uncased_L-12_H-768_A-12',
            'max_seq_length' : None, 
            'feat_dim': 768,
            'freeze_bert_parameters': True,
            'warmup_proportion': 0.1,
            'pretrain': False,
            'rtr_prob': 0.25,
            'train_batch_size' : 128,
            'pretrain_batch_size' : 128,
            'eval_batch_size' : 128,
            'test_batch_size': 128,
            'pre_wait_patient' : 20,
            'num_pretrain_epochs': 100,
            'num_train_epochs': 80,
            'lr_pre': 5e-5,
            'lr': 5e-5, 
            'num_iters_sk' : 3,
            'epsilon_sk' : 0.05,
            'imb_factor' : 1
        }

        return hyper_parameters