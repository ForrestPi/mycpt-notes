
### 文件打开方式
1. ios::app 以追加的方式打开文件
2. ios::ate 文件打开后定位到文件尾部，ios::app 包含这个属性
3. ios::binary 使用二进制的方式来读取，默认的格式是**文本格式**
4. ios::out 文件以输出的方式打开
5. ios::nocreate 不建立文件，如果文件不存在，就报错
6. ios::noreplace  不覆盖文件，所以打开文件，如果文件存在就失败
7. ios::trunc 如果文件存在，就把文件长度设为0

### 文件位置
1. ios::beg 文件开头
2. ios::cur 文件当前位置
3. ios::end 文件结尾
