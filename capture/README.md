# python3 简单爬虫
> [参考博客](https://cuiqingcai.com/5052.html)
### 请求库【首先把目标网页拿过来】
* `requests`: Py请求库，是一个阻塞式HTTP请求库，当我们发出一个请求后，程序会一直等待服务器响应，直到得到响应，程序才会进行下一步处理。
  ```
  pip3 install requests
  ```
* `selenium`: 自动化测试工具，利用他我们可以驱动浏览器执行待定的动作，如：点击、下拉等操作。
  ```
  pip3 install selenium
  ```
* `ChromeDriver`: 它是Chrome的浏览器驱动，有了他， 才能配合`selenium`使用。[安装教程](https://cuiqingcai.com/5135.html)
  * [win64的下载地址](https://www.pc18.com/soft/36193.html)
* `PhantomJS`: 一个无界面的、可脚本编程的WebKit浏览器引擎，原生支持多种WebKit标准：DOM操作、CSS选择器、JSON、Canvas以及SVG[安装教程](https://cuiqingcai.com/5159.html)。
  * `Selenium`支持`PhantomJS`，这样在运行时就不会弹浏览器出来啦。
  * `PhantomJS` 运行效率高，支持各种配置，使用方便。
* `aiohttp`:
  * 一个提供异步Web服务的库
  * 从Py3.5开始，Py加入了`async/await`关键字，使得回调写法更直观和人性化。`aiohttp`的异步操作借助于这两个关键字的写法变得更加简洁。
  * 目的：提高爬虫效率。

### 解析库【网页到手了，下一步是解析内容】
* `lxml`: Py的一个解析库，支持HTML和XML的解析，支持XPath解析方式，并且解析效率很高。
  ```
  pip install lxml
  ```
* `Beautiful Soup`: 是Py的一个HTML/XML解析库，拥有更强大的PI和多样的解析方式。他的HTML和XML解析器是依赖于lxml的。
  ```
  pip install beautifulsoup4
  ```
* `pyquery`: 一个强大的网页解析工具，提供了和jQuery类似的语法来解析HTML文档，支持CSS选择器，使用方便。
  ```
  pip install pyquery
  ```
* `tesserocr`:
  * 首先了解一些什么是OCR？ Optical Character Recognition， 光学字符识别，是指：通过扫描字符，然后通过其形状将其翻译成电子文本的过程。（就是读懂别人的验证码）
  * 利用OCR技术，我们就能自动识别验证码了
  * `tesserocr` 是Py的一个OCR识别库，但其实是对`tesseract`做的一层Python API封装而已，所以他的核心还是`tesseract`。
  * [安装过程](https://cuiqingcai.com/5189.html)

### 存储库
* `PyMongo`
  ```
  pip install pymongo
  ```

### Web库【搭Web程序，写API了】
* Flask：一个轻量级 Web 服务程序，主要用于做一些API服务。