sizeof的东西会被编译器直接替换掉，即使是汇编代码都只能看到一个常量，所以下面有童鞋说看反汇编源码是不行的，因为已经在编译器内部替换掉了（更严谨的说法是，VLA是特殊情况，这是后面的代码说明中有提到）。下面以Clang对sizeof的处理来看sizeof的实现。

作者：蓝色
链接：https://www.zhihu.com/question/26090484/answer/51261708
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
