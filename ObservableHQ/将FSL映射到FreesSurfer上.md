## 将FSL统计结果映射到FreesSurfer皮层上

这是一个工作过程记录。
总的目的是将`FSL`的预处理及统计分析结果，
映射到`FreeSurfer`的皮层空间上。

工作流可见我的[GITHUB工程](https://github.com/listenzcc/freesurferAnalysisScripts "GITHUB工程")，
可视化代码可见我的[ObservableHQ工程](https://observablehq.com/@listenzcc/free-surfer-cortex-v2 "ObservableHQ工程")。

---

- [将FSL统计结果映射到FreesSurfer皮层上](#将fsl统计结果映射到freessurfer皮层上)
  - [FreeSurfer Analysis Trace](#freesurfer-analysis-trace)
  - [Prepare Data](#prepare-data)
  - [Cortex visualization](#cortex-visualization)
  - [FSL portable](#fsl-portable)
    - [Projection from the nifti file to the surface](#projection-from-the-nifti-file-to-the-surface)

### FreeSurfer Analysis Trace

The project records the analysis trace for the `FreeSurfer` analysis.

---

### Prepare Data

The `T1 MRI Image` is required to make the cortex surfer.
The first step is fit the data into the format of `FreeSurfer`.

1. To do that, it is required to make the private `subject` folder in the `$FreeSurfer_HOME/Subjects` dir;
2. And generate the structure as `{subject}/mri/orig`;
3. Put the `T1 Image` into it, and name it like `001.mgz`,
   the script of [./shells/initFolderFreeSurferSubject.sh](./shells/initFolderFreeSurferSubject.sh) is generated to do the stuff;
4. The `.mgz` file is converted from `.nii` format by the shell tools named as `mri_convert`;
    ```sh
    # Convert the T1 MRI image <src> into <dst> file
    # The <src> file can be .nii file
    # Make sure the <dst> ends with .mgz
    mri_convert <src> <dst>
    ```
5. Finally, just operate the magic command `recon-all -s {subject} -all` and the jobs will be done;
6. Beware that the operation costs times, like **hours**;
7. After the operation, the `{subject}` folder will be filled with the files ready for everything.

If everything is alright,
The `{subject}` folder will follow the structure as below

| name | path                 | description |
| ---- | -------------------- | ----------- |
|      | ./scripts            |             |
|      | ./mri                |             |
|      | ./mri/transforms     |             |
|      | ./mri/transforms/bak |             |
|      | ./mri/orig           |             |
|      | ./surf               |             |
|      | ./tmp                |             |
|      | ./label              |             |
|      | ./touch              |             |
|      | ./stats              |             |
|      | ./trash              |             |

I will fill the blank table in later, (maybe not).

---

### Cortex visualization

The `freeview` tool provides amazing GUI to display the cortex surface.

---

### FSL portable

If you prefer using the `FSL` to do the fMRI analysis,
it provides the registration method to register the `feat` into cortex surface.

I use 2-steps operation to do the job

1. Link the directory of feat of `FSL`,
   use the script of [./shells/linkFeatDirs.sh](./shells/linkFeatDirs.sh);

2. Register the .nii.gz files in the feat directory to the subject of `FreeSurfer`,
   use the script of [./shells/registerFeatdir.sh](./shells/registerFeatdir.sh).

Basically, the functional of `reg-feat2anat` is used to do the registration

```sh
reg-feat2anat --feat $featdir --subject $subject
```

And it generates the nifti files in the folder of `$featdir/reg_surf-<lh | rh>-<$subject | fsaverage>`.
The nifti has a very strange format of `1974 x 1 x 83 = 163842` for the fsaverage version.
The document reads below

> In this case, the common space is the left hemisphere of fsaverage.
> Surface-based smoothing of 5mm FWHM is used.
> The output lh.cope1.mgh looks like a volume because it is in mgh format, but it is really a surface stored in a volume format (note it's dimensions are 1974 x 1 x 83 = 163842 = number of vertices in fsaverage's surface).

The nifti file can be read by the python package of `babel`,
and the script of [./read_nii.py](./read_nii.py) gives an example.

#### Projection from the nifti file to the surface

**Todo: I do not quite sure how to align the `1974 x 1 x 84` matrix with the `163842` vertex in the fsaverage's surface.**
**Will `arr.flatten()` do the job?**

The answer is NO,
actually, the following code will put the values into the **RIGHT** position

```js
const raw = await FileAttachment("zstat1.nii.gz.csv").csv();
const arr = [];
// This explains how to align .nii.gz matrix into the vertex array
for (let j = 0; j < 83; j++) {
    for (let i = 0; i < 1974; i++) {
        arr.push(1.0 * raw[i][j]);
    }
}
return arr;
```

One example of projection to the surface is like below

![FSL2FreeSurfer](./FSL2FreeSurfer.png)