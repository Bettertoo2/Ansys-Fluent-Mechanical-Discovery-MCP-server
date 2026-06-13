# 已废除-->请移步至https://github.com/Bettertoo2/ansys-mcp-server

# ANSYS MCP Server

ANSYS MCP Server 是一个基于 Model Context Protocol (MCP) 的服务器，用于驱动 ANSYS 系列仿真软件，包括 Fluent、Mechanical 和 Geometry。
# 目前仅支持v242（即2024r2）及其后续版本

## 功能特性

### Fluent (CFD)
- 启动/连接 Fluent solver
- 加载 case/mesh 文件
- 设置求解器参数（湍流模型、能量方程、瞬态/稳态）
- 设置边界条件和材料
- 初始化流场、迭代计算
- 获取残差值
- 保存 case/data
- 执行 TUI 命令
- 加载和管理 UDF

### Mechanical (网格划分)
- 启动/连接 Mechanical（支持连接已运行的实例）
- 导入几何文件
- 分配材料
- 划分网格
- 施加载荷和约束
- 执行求解
- 提取结果（变形、应力、应变）
- 执行 IronPython 脚本

> **提示：** 连接已运行的 Mechanical 实例时，需要先在 Mechanical 中启动 gRPC 服务器。详见 [辅助脚本](#辅助脚本) 章节。

### Geometry (几何建模)
- 启动 Geometry 建模器
- 创建几何设计
- 创建基本几何体（方块、圆柱、球体）
- 导入/导出 CAD 文件

## 安装

### 1. 创建虚拟环境

```bash
python -m venv .venv
```

### 2. 激活虚拟环境

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 配置

### Claude Desktop 配置

复制 `.mcp.json.example` 为 `.mcp.json`，并修改以下配置：

```json
{
  "mcpServers": {
    "ansys-mcp": {
      "command": "path/to/.venv/Scripts/python.exe",
      "args": ["-u", "path/to/server.py"],
      "env": {
        "AWP_ROOT242": "path/to/ANSYS/Inc/v242",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

### 环境变量

- `AWP_ROOT242`: ANSYS 安装路径（如 `C:\Program Files\ANSYS Inc\v242`）

## 使用方法

启动 MCP 服务器后，可以通过 Claude Desktop 或其他 MCP 客户端调用以下工具：

### Fluent 工具
- `fluent_launch`: 启动或连接 Fluent
- `fluent_read_case`: 加载算例文件
- `fluent_read_mesh`: 加载网格文件
- `fluent_set_solver`: 设置求解器参数
- `fluent_set_boundary`: 设置边界条件
- `fluent_set_material`: 设置材料
- `fluent_initialize`: 初始化流场
- `fluent_iterate`: 迭代计算
- `fluent_get_residuals`: 获取残差
- `fluent_save`: 保存文件
- `fluent_tui`: 执行 TUI 命令
- `fluent_load_udf`: 加载 UDF
- `fluent_hook_udf`: 挂钩 UDF 到边界
- `fluent_list_udfs`: 列出 UDF 状态
- `fluent_status`: 查看状态
- `fluent_exit`: 关闭 Fluent

### Mechanical 工具
- `mechanical_launch`: 启动或连接 Mechanical
- `mechanical_import`: 导入几何
- `mechanical_set_material`: 分配材料
- `mechanical_mesh`: 划分网格
- `mechanical_apply_load`: 施加载荷
- `mechanical_solve`: 执行求解
- `mechanical_get_result`: 提取结果
- `mechanical_list`: 列出几何体/Named Selections
- `mechanical_script`: 执行脚本
- `mechanical_status`: 查看状态
- `mechanical_exit`: 关闭 Mechanical

### Geometry 工具
- `geometry_launch`: 启动 Geometry 建模器
- `geometry_create_design`: 创建设计
- `geometry_create_block`: 创建方块
- `geometry_create_cylinder`: 创建圆柱
- `geometry_create_sphere`: 创建球体
- `geometry_export`: 导出几何
- `geometry_list_bodies`: 列出几何体
- `geometry_import_file`: 导入 CAD 文件
- `geometry_status`: 查看状态
- `geometry_close`: 关闭建模器

## 注意事项

1. 需要安装 ANSYS 2024 R2 (v242) 或更高版本
2. Fluent、Mechanical 和 Geometry 需要分别启动
3. 首次使用时，ANSYS 可能需要较长时间启动
4. 确保 ANSYS 许可证有效

## 辅助脚本

`scripts/` 目录包含辅助脚本，用于配置和启动 ANSYS 服务。

### mechanical_start_grpc.py

**功能：** 在 Ansys Mechanical 中启动 gRPC 服务器并获取端口号。

**使用场景：** 当需要连接到已运行的 Mechanical 实例时（而非启动新实例），需要先在 Mechanical 中启动 gRPC 服务器。

**使用方法：**

1. **打开 Ansys Mechanical**
   - 启动 Ansys Mechanical 应用程序
   - 打开或创建一个项目

2. **打开 Scripting 控制台**
   - 在 Mechanical 中，点击菜单：`View` → `Scripting`
   - 或使用快捷键打开脚本编辑器

3. **执行脚本**
   - 将 `scripts/mechanical_start_grpc.py` 中的内容复制到脚本编辑器
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

**脚本内容：**
```python
port_number = Ansys.ACT.Mechanical.MechanicalAPI.Instance.ApplicationAPI.StartGrpcServer()
print(f"Mechanical gRPC Server started on port: {port_number}")
print(f"Use this port number to connect via: mechanical_launch(port={port_number})")
```

**注意事项：**
- 该脚本需要在 Ansys Mechanical 内部执行，不能在外部 Python 环境中运行
- 端口号由系统自动分配，每次启动可能不同
- 确保防火墙允许该端口的通信
- gRPC 服务器启动后会一直运行，直到 Mechanical 关闭

## 许可证

MIT License
