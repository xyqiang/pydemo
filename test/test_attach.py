import pytest,allure

def test_attach_text():
    allure.attach("文本说明",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<html><head>网页</head></html>",attachment_type=allure.attachment_type.HTML)

def test_attach_img():
    allure.attach.file("./test.png",attachment_type=allure.attachment_type.PNG)

def test_attach_video():
    allure.attach.file("./test.mp4",attachment_type=allure.attachment_type.MP4)
