# ANSYS MCP Scripts

本目录包含辅助脚本，用于配置和启动 ANSYS 服务。

## mechanical_start_grpc.py

### 功能
在 Ansys Mechanical 中启动 gRPC 服务器并获取端口号。

### 使用场景
当需要连接到已运行的 Mechanical 实例时（而非启动新实例），需要先在 Mechanical 中启动 gRPC 服务器。

### 使用方法

1. **打开 Ansys Mechanical**
   - 启动 Ansys Mechanical 应用程序
   - 打开或创建一个项目

2. **打开 Scripting 控制台**
   - 在 Mechanical 中，点击菜单：`View` → `Scripting`
   - 或使用快捷键打开脚本编辑器

3. **执行脚本**
   - 将 `mechanical_start_grpc.py` 中的内容复制到脚本编辑器
   - 执行脚本
   - 记录输出的端口号（例如：`Mechanical gRPC Server started on port: 50052`）

4. **连接 MCP Server**
   - 使用 Claude Desktop 或其他 MCP 客户端
   - 调用 `mechanical_launch` 工具并指定端口：
     ```json
     {
       "port": 50052
     }
     ```

### 注意事项
- 该脚本需要在 Ansys Mechanical 内部执行，不能在外部 Python 环境中运行
- 端口号由系统自动分配，每次启动可能不同
- 确保防火墙允许该端口的通信
- gRPC 服务器启动后会一直运行，直到 Mechanical 关闭

### 示例输出
```
Mechanical gRPC Server started on port: 50052
Use this port number to connect via: mechanical_launch(port=50052)
```
