# Mechanical gRPC Server Startup Script
# 用于在 Ansys Mechanical 中启动 gRPC 服务器并获取端口号
#
# 使用方法：
# 1. 在 Ansys Mechanical 中打开 Scripting 控制台
# 2. 执行此脚本
# 3. 记录输出的端口号
# 4. 使用 mechanical_launch 工具连接该端口

port_number = Ansys.ACT.Mechanical.MechanicalAPI.Instance.ApplicationAPI.StartGrpcServer()
print(f"Mechanical gRPC Server started on port: {port_number}")
print(f"Use this port number to connect via: mechanical_launch(port={port_number})")
