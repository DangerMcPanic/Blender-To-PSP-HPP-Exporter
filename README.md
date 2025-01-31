This is an exporter for Blender that exports to a hpp file, the exported hpp can be used for rendering static 3d models on a PsP.

The contents of an exported hpp includes the indices clock-wise and counter-clock-wise, the indices count, and mesh as an array of vertices containing the UV, color and position.

HOW TO USE:
1. Open Blender and go to the "Scripting" tab
![bild](https://github.com/user-attachments/assets/a68877c0-b2bd-4c52-8d7a-004583f94fce)

2. Click the "Open" and locate the exporter from this repo
![bild](https://github.com/user-attachments/assets/f5378579-0337-4b00-bde7-95a8e24a9da3)

3. Make sure you are in "Object Mode" and have the object selected in the viewport, if you are in edit mode Blender will throw an error. The exporter will triangulate your mesh if it isn't already triangulated.
4. Now you can export to hpp by clicking this button.
![bild](https://github.com/user-attachments/assets/1051abed-c696-486e-b822-f3f6c7bb8244)

5. The contents of the exported file should look something like this, the exporter gets the name from the object name + "_Model"and there might be issues if it contains numbers or dots etc.
![bild](https://github.com/user-attachments/assets/4700550b-0d5d-42b8-b39c-9adeddb518f7)

6. Include your hpp like you would any other header. Now you can use the model with sceGumDrawArray/glDrawElements.
![bild](https://github.com/user-attachments/assets/69395957-30ed-43f1-a697-11a36a0b69b8)

TIPS:
You can bake materials/shaders/painting to a texture and resize it in Blenders UV tab
![bild](https://github.com/user-attachments/assets/d9c72c12-e5fe-4da8-8868-9f15ebbee320)
![bild](https://github.com/user-attachments/assets/3b63e8c4-785c-4178-97ff-be91d87cc962)
![bild](https://github.com/user-attachments/assets/447f234a-a81c-453d-a84a-616f2d40dfef)

Save the texture in a size that the PsP will accept such as 256x256

![bild](https://github.com/user-attachments/assets/06ba5e2e-1141-4f2b-a71b-2cc62236cf4a)
