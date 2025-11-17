# 中期记忆（活跃）

> 最后更新：2025-11-17T14:30:00Z

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

### AI模型注册和排序规范
**ID**: mem_20251117_004
**来源**: 【小黑：本地】@ 2025-11-17
**标签**: ai-models, registry, configuration, best-practices

**简述**: AI模型注册表配置规范：按能力排序、默认模型统一配置、上游检查流程

**模型注册规范**：
- 所有模型按能力从弱到强排序（priority 值递增）
- Priority 范围：10（最弱）到 80（最强）
- 排序标准：上下文窗口大小、能力数量、能力类型（STRUCTURED_OUTPUT > VISION > FUNCTION_CALLING）

**已注册模型（按能力排序）**：
1. GPT-4o Mini (priority=10) - 128K上下文，基础能力
2. GPT-5 Nano (priority=20) - 400K上下文，结构化输出
3. Gemini 2.0 Flash Lite (priority=30) - 1M上下文
4. Gemini 2.0 Flash (priority=40) - 1M上下文
5. Gemini 2.0 Flash Exp (priority=50) - 1M上下文，推荐模型
6. Gemini 2.5 Flash (priority=60) - 1M上下文
7. Grok 4 Fast (priority=70) - 2M上下文，无视觉
8. Gemini 2.5 Pro (priority=80) - 2M上下文，最强能力

**默认模型配置**：
- 统一默认模型：`openai/gpt-4o-mini`
- 涉及文件：
  * `backend/core/utils/project_helpers.py` (第26行)
  * `backend/core/utils/icon_generator.py` (第133行)
  * `backend/core/agent_setup.py` (第47行)

**上游检查流程**：
- check-upstream.md 已配置检查上述3个文件的默认 model_name
- 合并上游更新后自动验证默认模型配置
- 确保硬编码的 model_name 保持为 `"openai/gpt-4o-mini"`

**状态**: ✓ 已实施

## 已解决问题

### Windows Git 中文乱码问题解决
**ID**: mem_20251117_003
**来源**: 【小黑：本地】@ 2025-11-17
**标签**: git, windows, encoding, utf-8, troubleshooting

**简述**: Windows Git 中文乱码：原因（GBK/UTF-8冲突）、解决方案（Git/PowerShell/CMD UTF-8配置）、已解决

**问题原因**：
- Windows 终端默认 GBK（936），Git 提交消息使用 UTF-8
- Git 未配置编码设置
- PowerShell/CMD 未设置 UTF-8

**解决方案**：
- Git：`i18n.commitencoding=utf-8`, `i18n.logoutputencoding=utf-8`
- PowerShell：配置文件设置 UTF-8 编码
- CMD：注册表设置代码页 65001
- 修复乱码提交：使用 `git commit --amend -F` 通过文件传递

**状态**: ✓ 已解决

**详情**: 见 archives/xiaohei_local/2025-11-17_001.md

## 环境配置

（暂无）

---
**总计**: 4条中期记忆
