# playwright_generated_tests
How to generate tests using playwright

1) Check webpage "https://playwright.dev/python/docs/codegen-intro"

2) Type this command to start the code gereation playwright
# source python_venv_dir/bin/activate
# pip install playwright
# playwright codegen www.xe.com

3) 2 apps are launched:
    1) playwright inspector
    2) another browser with the www.xe.com address

4) View the playwright inspector. It already has code to start and close the browser. The "record" button is red which means whatever actions you do in the other browser will be recorded in the inspector.

5) After finishing the clicking, stop recording. Copy and paste the code and execute it using python. You'll reproduce exactly what you just typed.