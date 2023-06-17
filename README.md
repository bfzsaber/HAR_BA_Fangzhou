# Bachelor Thesis: TinyHAR on FPGA

||Start||End||
||01.07.2023*||31.10.2023*||
*planned

## BACKGROUND

**Human activity recognition (HAR)**
<!-- short introduction what is sensor based HAR - importance of HAR - importance of real time HAR -->
- HAR (Human Activity Recognition)  is a field of research and technology that focuses on the automatic detection, classification, and analysis of human activities based on various data sources
- In sensor-based HAR, various types of sensors, such as accelerometers, gyroscopes, magnetometers etc. are used to capture data related to human movements and actions.
- Real-time Human Activity Recognition (HAR) is crucial as it enables immediate response and intervention based on recognized activities. It enhances safety, security, performance, and user experience by allowing systems to react promptly, adapt to changing situations, optimize resource allocation, and provide personalized services.

**Field Programmable Gate Array (FPGA)** what is 
<!-- FPGA - why FPGA -->
- Field Programmable Gate Arrays (FPGAs) are integrated circuits that can be configured and reconfigured to perform different tasks. They offer several advantages, including high parallelism, low power consumption, and real-time processing capabilities. FPGAs are well-suited for implementing hardware accelerators for computationally intensive tasks like HAR.
## MOTIVATION
<!-- introduction of why is your topic valuable -->
The motivation behind this thesis is to explore the implementation of TinyHAR (a lightweight human activity recognition algorithm) on an FPGA platform. By leveraging the parallel processing capabilities of FPGAs, it is possible to accelerate the execution of TinyHAR and achieve real-time performance.

## METHODOLOGY
1.  **Model Selection and Dataset Preparation:** I choose the TinyHAR model and use public datasets such as PAMAP2, WISDM, and Opportunity for comprehensive analysis.
2.  **implement Neural Networks on FPGAs:** I plan to explore toolflows like FINN from Xilinx to lower the design burden while implementing Neural Networks onto FPGAs.
3.  **Optimizing the FPGA Accelerator:** After implementing, we aim to enhance the FPGA accelerator, focusing on its parallel computing ability.
4.  **Performance Comparison:** Finally, we will compare our FPGA-based HAR model to traditional CPU and MCU-based systems in terms of speed and energy efficiency.

## CONTREIBUTION
The main contribution of this work is the implementation of TinyHAR on an FPGA platform, showcasing the benefits of using FPGAs for real-time HAR. The thesis will provide insights into the challenges and opportunities associated with FPGA-based acceleration for HAR applications. It will also demonstrate the potential for achieving low-latency and energy-efficient solutions using FPGA technology.


## WORK PLAN
~~Week 1-12 corresponds to the period from June 19th to September 10th.~~
~~even though the registered time is from July 1st to October 30th~~
| Task | Start Date | End Date  | Duration (Days) |
|-----------------|-----------------|-----------------|-----------------|
| TinyHAR Brevitas_ONNX export| | |week1|
|(based on the limitation of FINN, designing plans and deadlines to solve the problem) plan a: Model Partition - which node? How| | |week2|
|Model Partition - how to combine child models, how to verify, how to implement(theory)|||week 3 |
|Model Partition - adjusting parameters according to theories and implementation|||week4
|FPGA Board Exploration or explore other evaluation methods|||week5|
|design approperiate metric|||week6|
|evaluate the proposed metrics|||week 7 +8|
|writing thesis|||week 9 10 11 12|
## CORE TASK

- Find the suitable datasets 
- Implement the proposed algorithm
- Design approperiate metric 
- Evaluate the proposed framework 
- Write thesis

## RISKS (continuously updated)

>For each foreseable risk (try to name as many as possible, at least 3) causing either delays or not fulfilling parts of the plan a description should be maintained
>||Risk Description||Impact||Likelyhood||Preventive Measure||Reactive Measure||Status||
>||ill-conditioned gradient modification|| non-convergence of training || likely || hyper-parameter tuning ||N/A||N/A
>||weights are not well-similated|| bad result || likely || hyper-parameter tuning ||N/A||N/A
