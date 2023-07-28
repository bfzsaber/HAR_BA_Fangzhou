
Brevitas

args.cross_channel_interaction_type = "attn"
args.cross_channel_aggregation_type = "FC"
args.temporal_info_interaction_type = "conv"
args.temporal_info_aggregation_type = "tnaive"

average marco f1 72.91% +- 1.17%
Computational complexity(MAC):       389440.0
Number of parameters:           40008 


args.model_type              = "tinyhar"

args.cross_channel_interaction_type = "attn"
args.cross_channel_aggregation_type = "FC"
args.temporal_info_interaction_type = "lstm"
args.temporal_info_aggregation_type = "tnaive"
Average macro F1:6.3958594 / 9 ≈ 0.710651044

TinyHAR paper:
model size(Number of trainable parameters): 37274
FLOP: 1466764
#
- (same setting) original TinyHAR:  Average Test macro F1 = 6.5619469 / 9 = 0.729105211

0 Final Test Performance : Test Accuracy: 0.7906664  Test weighted F1: 0.7903274  Test macro F1 0.7899795 

1 Final Test Performance : Test Accuracy: 0.8620124  Test weighted F1: 0.8594191  Test macro F1 0.8620604

2 Final Test Performance : Test Accuracy: 0.8829846  Test weighted F1: 0.8874548  Test macro F1 0.5896113 

3 Final Test Performance : Test Accuracy: 0.8069266  Test weighted F1: 0.8078372  Test macro F1 0.7366537 

4 Final Test Performance : Test Accuracy: 0.8747575  Test weighted F1: 0.8757632  Test macro F1 0.8707761 

5 Final Test Performance : Test Accuracy: 0.8645273  Test weighted F1: 0.8636275  Test macro F1 0.7831808 

6 Final Test Performance : Test Accuracy: 0.8938893  Test weighted F1: 0.8900698  Test macro F1 0.7913788 

7 Final Test Performance : Test Accuracy: 0.8047977  Test weighted F1: 0.7996611  Test macro F1 0.7852025 

8 Final Test Performance : Test Accuracy: 0.8721805  Test weighted F1: 0.9317269  Test macro F1 0.1331038
# 
### brevitas 1
0 Final Test Performance : Test Accuracy: 0.7998848  Test weighted F1: 0.7956729  Test macro F1 0.8062670 

1 Final Test Performance : Test Accuracy: 0.8514400  Test weighted F1: 0.8507447  Test macro F1 0.8522278 

2 Final Test Performance : Test Accuracy: 0.8348018  Test weighted F1: 0.8380871  Test macro F1 0.5598076 

3 Final Test Performance : Test Accuracy: 0.8950643  Test weighted F1: 0.8960755  Test macro F1 0.8112789 

4 Final Test Performance : Test Accuracy: 0.8520021  Test weighted F1: 0.8530322  Test macro F1 0.8540827

5 Final Test Performance : Test Accuracy: 0.8608762  Test weighted F1: 0.8613532  Test macro F1 0.7819123 

6 Final Test Performance : Test Accuracy: 0.9163914  Test weighted F1: 0.9170584  Test macro F1 0.8997505 

7 Final Test Performance : Test Accuracy: 0.8047977  Test weighted F1: 0.7934629  Test macro F1 0.7805402

8 Final Test Performance : Test Accuracy: 0.7293233  Test weighted F1: 0.8434783  Test macro F1 0.0937198 

0.8062670 + 0.8522278 + 0.5598076 + 0.8112789 + 0.8540827 + 0.7819123 + 0.8997505 + 0.7805402 + 0.0937198 = 6.4395878
Average Test macro F1 = 6.4395878 / 9 = 0.71550976
#
### brevitas 2
0 Final Test Performance : Test Accuracy: 0.8563472  Test weighted F1: 0.8605434  Test macro F1 0.8629743 

1 Final Test Performance : Test Accuracy: 0.8769595  Test weighted F1: 0.8719014  Test macro F1 0.8645477 

2 Final Test Performance : Test Accuracy: 0.8136013  Test weighted F1: 0.8175388  Test macro F1 0.5426811 

3 Final Test Performance : Test Accuracy: 0.8641642  Test weighted F1: 0.8637812  Test macro F1 0.8629357 

4 Final Test Performance : Test Accuracy: 0.8668195  Test weighted F1: 0.8695917  Test macro F1 0.8653647 

5 Final Test Performance : Test Accuracy: 0.8195619  Test weighted F1: 0.8120433  Test macro F1 0.7450309 

6 Final Test Performance : Test Accuracy: 0.9130884  Test weighted F1: 0.9140420  Test macro F1 0.8951568 

7 Final Test Performance : Test Accuracy: 0.8351950  Test weighted F1: 0.8346671  Test macro F1 0.8177919 

8 Final Test Performance : Test Accuracy: 0.5639098  Test weighted F1: 0.7211538  Test macro F1 0.0721154 

Average Test macro F1 = 6.6286088 / 9 = 0.7365120889
#
### brevitas 3
0 Final Test Performance : Test Accuracy: 0.8361821  Test weighted F1: 0.8387450  Test macro F1 0.8458998

1 Final Test Performance : Test Accuracy: 0.8149836  Test weighted F1: 0.8059561  Test macro F1 0.8067456 

2 Final Test Performance : Test Accuracy: 0.8507709  Test weighted F1: 0.8543520  Test macro F1 0.5687570 

3 Final Test Performance : Test Accuracy: 0.8859394  Test weighted F1: 0.8872295  Test macro F1 0.8861027 

4 Final Test Performance : Test Accuracy: 0.8363027  Test weighted F1: 0.8366449  Test macro F1 0.8403473 

5 Final Test Performance : Test Accuracy: 0.8299385  Test weighted F1: 0.8352845  Test macro F1 0.7652165 
 
6 Final Test Performance : Test Accuracy: 0.9271263  Test weighted F1: 0.9295111  Test macro F1 0.9058405 

7 Final Test Performance : Test Accuracy: 0.7765977  Test weighted F1: 0.7514954  Test macro F1 0.7440763 

8 Final Test Performance : Test Accuracy: 0.6992481  Test weighted F1: 0.8230088  Test macro F1 0.1028761 

Average Test macro F1 = 6.6668628 / 9 = 0.740762533
#
### brevitas 4
0 Final Test Performance : Test Accuracy: 0.8327252  Test weighted F1: 0.8334829  Test macro F1 0.8377879 

1 Final Test Performance : Test Accuracy: 0.8773241  Test weighted F1: 0.8759174  Test macro F1 0.8699003 

2 Final Test Performance : Test Accuracy: 0.8783040  Test weighted F1: 0.8824507  Test macro F1 0.6391535 

3 Final Test Performance : Test Accuracy: 0.8490253  Test weighted F1: 0.8524156  Test macro F1 0.7749387 

4 Final Test Performance : Test Accuracy: 0.8551773  Test weighted F1: 0.8568597  Test macro F1 0.8532545 

5 Final Test Performance : Test Accuracy: 0.7966949  Test weighted F1: 0.8017170  Test macro F1 0.7335925

6 Final Test Performance : Test Accuracy: 0.9184558  Test weighted F1: 0.9198657  Test macro F1 0.9111061 

7 Final Test Performance : Test Accuracy: 0.7480315  Test weighted F1: 0.7388522  Test macro F1 0.7275742 

8 Final Test Performance : Test Accuracy: 0.4962406  Test weighted F1: 0.6633166  Test macro F1 0.0663317

Average Test macro F1 = 6.6136404 / 9 = 0.734849044
#
### brevitas 5

0 Final Test Performance : Test Accuracy: 0.8171692  Test weighted F1: 0.8091432  Test macro F1 0.8171930 

1 Final Test Performance : Test Accuracy: 0.7801677  Test weighted F1: 0.7548043  Test macro F1 0.7619998 

2 Final Test Performance : Test Accuracy: 0.8598568  Test weighted F1: 0.8648021  Test macro F1 0.6274383 

3 Final Test Performance : Test Accuracy: 0.8954791  Test weighted F1: 0.8959631  Test macro F1 0.8106410 

4 Final Test Performance : Test Accuracy: 0.8371847  Test weighted F1: 0.8392552  Test macro F1 0.8375088

5 Final Test Performance : Test Accuracy: 0.8151422  Test weighted F1: 0.8091280  Test macro F1 0.7436316 

6 Final Test Performance : Test Accuracy: 0.9304294  Test weighted F1: 0.9312584  Test macro F1 0.8395721 

7 Final Test Performance : Test Accuracy: 0.7451016  Test weighted F1: 0.7251328  Test macro F1 0.7124973 

8 Final Test Performance : Test Accuracy: 0.7593985  Test weighted F1: 0.8632479  Test macro F1 0.1079060 


Average = Sum of Test macro F1 scores / Number of samples = 6.4583889 / 9 ≈ 0.7175988
