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
## WORK PLAN
~~Week 1-12 corresponds to the period from June 19th to September 10th.~~
~~even though the registered time is from July 1st to October 30th~~
| Week | Duration | Tasks  |  
|-----------------|-----------------|-----------------|
|~~week 01~~|~~19.06-25.06~~|-write quantized TinyHAR using Brevitas's library|
|~~week 02~~|~~26.06-02.07~~| -collect similar articles and projects using FINN<br> -analyse their solution for implementing model that is not entirely supported by FINN<br> -list their pros and cons, probability for TinyHAR model<br> -discuss with advisor to choose a solution for TinyHAR|
|~~week 03~~|~~03.07-09.07~~|-(Target given Zedboard: Zynq-7000 SOC)<br> -how to transfer data between MCU and FPGA|
|week 04|10.07-16.07|**criteria**: FINN pipeline<br> -use costum partition to separate TinyHAR model according to FINN-HLS library support<br> -hardware generation for HLS supported parts|
|week 05|17.07-23.07|-6 datasets, quantised TinyHAR vs original HAR metrics: Averaged F1M and model size<br> FPGA synthesis part, reports|
|week 06|24.07-30.07|**criteria**:evaluation comparison<br> - CPU and MCU or GPU Latency etc. and energy efficiency|
|week 07|31.07-06.08|for future works: combine FPGA and MCU parts on Zedboard|
|week 08|07.08-13.08||
|week 09|14.08-20.08|**criteria**：structure of the thesis<br> -reorganise from previous weekly report and list used literatures<br> -compare to similar works a.their structure b.FINN what is mentionable and proof their correctness|
|week 10|21.08 - 27.08|-study for theory background a.FPGA and HAR b.mathematic parts<br> -design challenges and implementation|
|week 11|28.08 - 03.09|**criteria**：initial draft of the thesis<br> -statistic, comparison<br> -conclusion, future works etc.<br> -combine different parts |
|week 12|04.09-10.09|-presentation preparation|
|week 13|11.09-19.09|**criteria**：-Thesis Defense|

## CORE TASK

- Find the suitable datasets 
- Implement the proposed algorithm
- Design approperiate metric 
- Evaluate the proposed framework 
- Write thesis

## RISKS (continuously updated)

For each foreseable risk (try to name as many as possible, at least 3) causing either delays or not fulfilling parts of the plan a description should be maintained

| Risk Description | Impact | Likelyhood | Preventive Measure | Reactive Measure | Status |
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|limitation from CNN_FPGA Tool flows: certain layers or functions are not supported|can not generate hardware file purely based on FPGA |very likely|N/A|a.write costume functions according to the tool flow b.run unsupported parts on CPU|N/A|
