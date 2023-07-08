# EEG 和 LFP 相互关系的动态展示

本文对 LFP（局部场电位）和EEG（脑电图）的理解进行简单的可视化，要表达的信息是 LFP 是大脑内部 $Na^+, Ca^{2+}$等离子有序迁移引起的局部电位变化，而 EEG 是在头皮表面，以无创的方法采集到的电场强度变化。

本文通过一段代码直观地展示了这一过程，你可以在这里找到它

[LFP & EEG](https://observablehq.com/@listenzcc/lfp-eeg)

---
- [EEG 和 LFP 相互关系的动态展示](#eeg-和-lfp-相互关系的动态展示)
  - [动画 Demo](#动画-demo)
  - [LFP 和 EEG 的区别与联系](#lfp-和-eeg-的区别与联系)
  - [LFP 和 EEG 的信号生成机制](#lfp-和-eeg-的信号生成机制)
  - [LFP 是不是 EEG 的成因？](#lfp-是不是-eeg-的成因)


## 动画 Demo

本文对 LFP（局部场电位）和EEG（脑电图）的理解进行简单的可视化，要表达的信息是 LFP 是大脑内部 $Na^+, Ca^{2+}$等离子有序迁移引起的局部电位变化，而 EEG 是在头皮表面，以无创的方法采集到的电场强度变化。下图中的圆圈代表大脑，其中的小球代表局部电位变化源，而表面的一圈小圆球代表 EEG 的导联布局，用来测量头皮表面的电场强度变化，接下来的视频则反映了这一动态过程。

![Untitled](EEG%20%E5%92%8C%20LFP%20%E7%9B%B8%E4%BA%92%E5%85%B3%E7%B3%BB%E7%9A%84%E5%8A%A8%E6%80%81%E5%B1%95%E7%A4%BA%20e7abdcc0d8a54d7e8f3ce24cab485be9/Untitled.png)

【这是一段视频】

## LFP 和 EEG 的区别与联系

> LFP stands for Local Field Potential, and EEG stands for Electroencephalography. Both are related to the measurement and recording of electrical activity in the brain.
> 

LFP 和 EEG 都是用于测量脑电活动的技术，它们具有区别和联系。针对这个问题，一篇 2012 年的论文 “**The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes**” 给出了很全面的综述。

[NCBI - WWW Error Blocked Diagnostic](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4907333/)

![**c** | Simultaneously recorded magnetoencephalogram (MEG; black) and anterior hippocampus depth EEG (red) from a patient with drug-resistant epilepsy. Note the similar theta oscillations recorded by the depth electrode and the trace calculated by the MEG, without any phase delay. 
**d** | Simultaneously recorded LFP traces from the superficial (‘surface’) and deep (‘depth’) layers of the motor cortex in an anaesthetized cat and an intracellular trace from a layer 5 pyramidal neuron. Note the alternation of hyperpolarization and depolarization (slow oscillation) of the layer 5 neuron and the corresponding changes in the LFP. The positive waves in the deep layer (close to the recorded neuron) are also known as delta waves. iEEG, intracranial EEG.](EEG%20%E5%92%8C%20LFP%20%E7%9B%B8%E4%BA%92%E5%85%B3%E7%B3%BB%E7%9A%84%E5%8A%A8%E6%80%81%E5%B1%95%E7%A4%BA%20e7abdcc0d8a54d7e8f3ce24cab485be9/Untitled%201.png)

**c** | Simultaneously recorded magnetoencephalogram (MEG; black) and anterior hippocampus depth EEG (red) from a patient with drug-resistant epilepsy. Note the similar theta oscillations recorded by the depth electrode and the trace calculated by the MEG, without any phase delay. 
**d** | Simultaneously recorded LFP traces from the superficial (‘surface’) and deep (‘depth’) layers of the motor cortex in an anaesthetized cat and an intracellular trace from a layer 5 pyramidal neuron. Note the alternation of hyperpolarization and depolarization (slow oscillation) of the layer 5 neuron and the corresponding changes in the LFP. The positive waves in the deep layer (close to the recorded neuron) are also known as delta waves. iEEG, intracranial EEG.

LFP 和 EEG 的区别在于：

1. 尺度：LFP是通过在脑组织的局部区域测量电势变化来获取的，通常使用微电极在小范围内记录。相比之下，EEG是通过在头皮上放置电极阵列来测量脑电活动，因此反映了大范围的神经活动。
2. 空间分辨率：由于LFP测量的是局部区域的电位变化，因此具有较高的空间分辨率。相比之下，EEG测量的是头皮上的电位变化，受到头骨、脑脊液等因素的干扰，因此空间分辨率较低。
3. 深度：LFP可以提供有关神经元活动在脑组织深度的变化的信息。它可以测量神经元兴奋和抑制的活动，提供更多关于神经元网络的局部细节。
4. 应用领域：LFP主要应用于动物研究，特别是用于研究局部神经回路和行为。EEG则广泛用于临床和研究领域，用于检测和诊断脑电活动的异常，如癫痫、睡眠障碍等。

它们的联系在于：

1. 电位测量：无论是LFP还是EEG，它们都是通过测量神经元活动产生的电位变化来获取脑电信号的。
2. 频率特征：LFP和EEG都可以显示不同频率的波形。LFP通常包括局部场电位振荡，如γ波、θ波等，而EEG则包括α波、β波、δ波等不同频率的脑电节律。
3. 数据分析：LFP和EEG数据都需要进行类似的数据处理和分析。常见的方法包括频谱分析、时频分析和相干性分析等。

总之，LFP和EEG都是测量脑电活动的方法，但它们在尺度、空间分辨率、深度和应用领域等方面存在一些差异。然而，它们都提供了对脑电活动的重要信息，对于研究神经科学和临床诊断都具有重要意义。

## LFP 和 EEG 的信号生成机制

LFP的信号生成机制：
LFP是由局部神经元的集体活动所产生的。当神经元集群同时发放动作电位时，它们产生的电流会在周围的组织中传播。这些电流在脑组织中的传播会引起细胞外液中的电势变化，形成LFP信号。LFP主要反映了局部神经元活动的总体情况，包括神经元的兴奋和抑制状态、突触传递和神经元网络的同步性等。

EEG的信号生成机制：
EEG是通过记录头皮上的电位变化来获取的。它反映了大范围神经元网络的同步活动。当大量神经元同时活动时，它们会产生电流，这些电流在头皮和脑组织之间传播，并且可以通过头皮上的电极被检测到。脑电信号经过头骨、脑脊液等组织的传导和滤波作用，最终形成记录在EEG上的波形。EEG信号通常包括多种频率的节律性振荡，如α波、β波、θ波和δ波等，这些节律反映了不同脑区的神经活动状态。

需要注意的是，LFP和EEG的信号生成机制都受到了许多因素的影响，包括神经元类型、神经元密度、突触连接、神经元活动的同步性、电极位置等。因此，理解LFP和EEG信号的生成机制需要综合考虑多种因素，并结合具体研究和分析方法进行解释。

## LFP 是不是 EEG 的成因？

LFP是在脑组织局部区域记录的电位变化，反映了该区域的神经元活动。当大量的神经元在某个局部区域同时活动时，它们产生的电流会在周围组织中传播，形成局部电位变化。这些电位变化可以通过放置在局部区域的微电极来记录。

然而，LFP信号在传播过程中会受到组织的滤波和耦合效应的影响。当电流通过头骨和脑脊液等组织传播时，它们会受到过滤和衰减，同时也会与其他局部区域的电流相互作用。这些因素导致LFP信号在传播到头皮上时发生进一步的变化。

在头皮上测量到的电位变化就是EEG信号。EEG记录的是头皮上大范围神经元活动的总体情况，包括不同脑区的神经元网络的同步活动。因此，EEG可以看作是由多个局部区域的LFP信号的叠加所形成的。

综上所述，LFP可以视为EEG信号的一部分，它是在脑组织局部区域产生的电位变化。这些局部电位变化在经过组织传导和滤波后形成了测量在头皮上的EEG信号。因此，LFP可以被认为是EEG信号的成因之一。