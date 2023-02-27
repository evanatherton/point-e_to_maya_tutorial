# Tutorial: Using [point-e](https://github.com/openai/point-e) in Autodesk Maya

This tutorial will get you started using point point-e in Autodesk Maya with Bifrost. point-e is OpenAI's text-to-3D model that generates point clouds from complex prompts.

In this tutorial we will:
- Use Maya's python script editor to send prompts to the point-e model using the [Replicate API](https://replicate.com/cjwbw/point-e)
- Create a Bifrost graph to store and visualize the resultant point cloud
- Explore some practical examples of how to manipulate the point clouds using Bifrost

Result are usually returned in around 1 minute, but the first run could take closer to 3 minutes. See Replicate's info on [Cold boots](https://replicate.com/docs/how-does-replicate-work#cold-boots) to find out more.

## Video Tutorial

[![Tutorial: text-to-3d in Maya with point-e and Bifrost](https://img.youtube.com/vi/f7Ku907tIFg/0.jpg)](https://youtu.be/f7Ku907tIFg)


If you just want to skip the video and just run the example graphs, follow these steps:

## Getting Started
This tuturial uses Maya 2023 and Bifrost 2.6, but should work with Maya 2022 and Bifrost 2.5 and later.
First we need to install the `replicate` library using `mayapy`, Maya's Python interpreter:

- On MAC: Open Terminal and run the following command:
    ```
    /Applications/Autodesk/maya2023/Maya.app/Contents/bin/mayapy -m pip install replicate
    ```

- On PC: Run Command Prompt as an administrator and run the following commands:
    ```
    "C:\Program Files\Autodesk\Maya2023\bin\mayapy.exe" -m pip install replicate
    ```

Next, verify replicate was installed correctly:

- Open Maya 2023
- In the script editor, run the following commands in a Python tab:

    ```
    import replicate
    ```

If you don't see an error, you should be good to go.

Lastly, you'll need a Replicate API token, which you can get by signing up for a Replicate account (or by logging in with your GitHub account), and going to your [Account](https://replicate.com/account) page.

## Running the example graph
- Download and open the `openai_point-e_tutorial.ma` file
- Copy/paste the `point_e_to_bif_tutorial.py` script into a python tab in Maya's script editor
- Copy/paste your Replicate API token between the single quotes in line 7 of the script: `API_KEY = ''`
- Run the script. A prompt dialog will appear with a default prompt. Type your prompt and hit `OK`. The results should update in Maya's viewport in ~1 minutes when the 
- You can find some sample Bifrost graphs in [examples](https://github.com/evanatherton/point-e_to_maya_tutorial/tree/main/examples) for some ideas on how to continue working with your point clouds in Maya

Note: the Plexus example graph requires the MJCG Compound pack, which you can download [here](https://mjcg.gumroad.com/l/mjcg_compounds)


