# -*- coding: utf-8 -*-
# __author__=luhu
"""
        如今大多数的web应用程序使用AJAX技术，当浏览器在加载页面时，页面的元素可能并不是同时被加载完成的，
    这给元素的定位添加了困难，如果因为在加载某个元素时延时而造成ElementNotVisibleException的情况出现，
    那么就降低了自动化脚本的稳定性。
        webdriver提供了两种类型的等待：显式等待和隐式等待。
        显式等待使webdriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时的异常(TimeoutException)
        WebdriverWait()是由webdriver提供的等待方法，在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，
        如果超过设置时长检测不到则抛出异常。具体格式如下：

            WebdriverWait()

            WebdriverWait(driver, timeout, poll_frequency = 0.5, ignored_exceptions = None)
            driver                  webdriver的驱动程序    driver = webdriver.Chrome()
            timeout                 最长超时时间，默认以秒为单位
            poll_frequecy           休眠时间的间隔（步长）时间，默认为0.5秒
            ignoread_exceptions     超时后的异常信息，默认情况下抛出NoSuchElementException异常。

            until()

            WebdriverWait()一般由until()(或until_not())方法配合使用，下面是util()和until_not()方法的说明：
                until(method, message = '')    调用该方法提供的驱动程序作为一个参数，直到返回true为止。
                until_not(method, message = '')    调用该方法提供的驱动程序作为一个参数，直到返回false为止。

            Expected  Conditions

                下面的例子，我们在使用expected_conditions类时对其重命名，通过as关键字对其重命名为EC，并调用
            presence_of_element_located()判断元素是否存在。
                 expected_conditions类提供一些预期条件的实现：
                    title_is                                    用于判断标题是否为XX
                    title_contains                              用于判断标题中是否包含XX信息
                    presence_of_element_located                 元素是否存在
                    visibility_of_element_located               元素是否可见
                    visibility_of                               是否可见
                    presence_of_all_element_located             判断一组元素是否存在
                    text_to_be_presence_in_element              判断元素是否有xx文本消息
                    text_to_be_presence_in_element_value        判断元素值是否有xx文本消息
                    frame_to_be_available_and_switch_to_it      表单是否可用，并切换到该表单
                    invisibility_of_element_located             判断元素是否隐藏
                    element_to_be_clickable                     判断元素是否可点击，它处于可见和启动状态
                    staleness_of                                等到一个元素不再是依附于DOM
                    element_to_be_selected                      被选中的元素
                    element_located_to_be_selected              一个期望的元素位于被选中
                    element_selection_state_to_be               一个期望检查如果给定的元素被选中
                    element_located_selection_state_to_be       期望找到一个元素并检查是否为选择状态
                    alert_is_present                            预期一个警告信息
            除了excepted_conditions所提供的预期方法，我们也可以使用前面学过的is_display方法来判断元素是否可见。
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 显式等待
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
input1 = driver.find_element_by_id('kww')
# lambda为匿名函数，:前面定义变量，后面定义函数,每隔一段时间都会调用一下这个匿名函数，
# 直到函数返回的值为true，或者超时抛出异常
element = WebDriverWait(driver, 5, 0.5).until(lambda s: input1.is_displayed())
input1.send_keys('my_selenium')
driver.quit()

# 隐式等待
"""
        implicitly_wait()默认参数的单位为秒，本例中设置等待时间为10秒，首先这10秒并非一个固定的等待时间，他并不
    影响脚本的执行速度。其次，它并不是真对页面上的某一元素进行等待，当脚本执行到某个元素定位时，如果元素可定位，
    那么继续执行，如果定位不到，那么他将以轮询的方式不断判断元素是否被定位到，如果被定位到就继续执行，超出定位设置
    时长10秒则抛出异常。
"""
driver =webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
input2 = driver.find_element_by_id('kww')
input2.send_keys('my_selenium')
driver.quit()




















