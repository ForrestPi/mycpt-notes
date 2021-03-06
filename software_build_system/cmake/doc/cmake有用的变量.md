### CMakeLists.txt 相关配置
#### CMAKE_BINARY_DIR
工程的输出目录.

#### CMAKE_CURRENT_BINARY_DIR
当前的 `CMakeLists.txt` 的输出目录, 因为可以包含子目录, 这个就是子工程的输出目录.

#### CMAKE_CURRENT_LIST_FILE
当前的 `CMakeLists.txt` 全路径名称.

#### CMAKE_CURRENT_LIST_DIR
当前的 `CMakeLists.txt` 所在目录.

#### CMAKE_CURRENT_SOURCE_DIR
当前的项目源代码目录.

```cmake
message(${CMAKE_CURRENT_LIST_FILE})
message(${CMAKE_CURRENT_LIST_DIR})
```

- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`
- ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) `#c5f015`
- ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `#1589F0`


---

### 编译器设置

#### CMAKE_CXX_COMPILER
配置c++编译器

```
set( CMAKE_CXX_COMPILER, "/usr/bin/g++" )
```

#### CMAKE_CXX_FLAGS

配置c++的编译选项

```
set( CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
```

#### CMAKE_C_FLAGS

```
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS -std=c99}")
```

---
