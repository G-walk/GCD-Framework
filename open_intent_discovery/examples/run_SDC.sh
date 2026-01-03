for dataset in  'banking'
do
    for known_cls_ratio in 0.75
    do
        for cluster_num_factor in   1.0
        do
            for seed in 0
            do 
                python run.py \
                --dataset $dataset \
                --method 'SDC' \
                --train \
                --setting 'semi_supervised' \
                --labeled_ratio 0.1 \
                --known_cls_ratio $known_cls_ratio \
                --cluster_num_factor $cluster_num_factor \
                --seed $seed \
                --backbone 'bert_SDC' \
                --config_file_name 'SDC' \
                --gpu_id '0' \
                --results_file_name 'SDC.csv' \
                --save_results \
                --save_model \
                --test
            done
        done
    done
done