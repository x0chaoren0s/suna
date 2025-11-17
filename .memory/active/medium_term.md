# 中期记忆（活跃）

> 最后更新：2025-11-17T05:13:33Z

## 工具和脚本

### 项目工具开发
**ID**: mem_20251117_001
**来源**: 【大黑-毕业win10：Ubuntu】@ 2025-11-17
**标签**: backup, pdf, markdown, tools

**简述**: 注册表备份/恢复脚本、PDF转MD工具方案

**组件**:
- backup-registry.py、restore-registry.py：备份 backend/core/ai_models/registry.py
- 想法.md：PDF转Markdown工具，用于suna框架存储论文

**详情**: 见 archives/dahei_biye_win10_ubuntu/2025-11-17_001.md

## 架构决策

### 跨终端记忆通信系统
**ID**: mem_20251117_002
**来源**: 【大黑-毕业win10：Ubuntu】@ 2025-11-17
**标签**: memory-system, cross-terminal, protocol, mvp

**简述**: 完整的跨终端记忆共享系统，协议设计与MVP实现

**核心组件**:
- MEMORY-PROTOCOL.md：1870行完整协议规范
- 三层记忆体系：短期（7天）、中期（项目级）、长期（通用）
- Git分支管理：独立memory分支
- 文件架构：config、index、archives、active
- MVP命令：SYNC、HARVEST

**设计特点**:
- 基于实际变更而非对话历史
- 终端配置独立管理（system.json不同步）
- 数据结构优化（无冗余）
- 模块化设计（自包含）

**详情**: 见 archives/dahei_biye_win10_ubuntu/2025-11-17_001.md

## 功能和特性

（暂无）

## 已解决问题

（暂无）

## 环境配置

（暂无）

---
**总计**: 2条中期记忆
