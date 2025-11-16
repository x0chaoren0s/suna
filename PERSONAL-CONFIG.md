# 个人配置指南

## 概述

本文档说明如何配置你的个人开发环境，包括代理、API 密钥、模型选择等。

**重要提示：** 所有个人配置都应该保存在本地配置文件中，**不要提交到 Git**！

## 配置文件位置

项目使用以下配置文件（已在 `.gitignore` 中，不会被提交）：

- `backend/.env` - 后端配置
- `frontend/.env.local` - 前端配置
- `apps/mobile/.env.local` - 移动应用配置（如果需要）

## 快速开始

### 方法 1: 使用 setup.py（推荐）

运行项目自带的设置脚本：

```bash
python setup.py
```

脚本会引导你完成所有配置，包括：
- Supabase 设置
- Daytona API 密钥
- LLM API 密钥
- 搜索 API 配置
- 其他可选服务

### 方法 2: 手动配置

#### 1. 后端配置 (`backend/.env`)

创建 `backend/.env` 文件并添加你的配置：

```bash
# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
SUPABASE_JWT_SECRET=your_jwt_secret

# Daytona（沙盒环境）
DAYTONA_API_KEY=your_daytona_key

# LLM API 密钥
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
OPENROUTER_API_KEY=your_openrouter_key
GOOGLE_API_KEY=your_google_key
# ... 其他 LLM 提供商

# 搜索 API
TAVILY_API_KEY=your_tavily_key
FIRECRAWL_API_KEY=your_firecrawl_key
SERPER_API_KEY=your_serper_key
EXA_API_KEY=your_exa_key

# 可选服务
RAPID_API_KEY=your_rapid_api_key
COMPOSIO_API_KEY=your_composio_key
MORPH_API_KEY=your_morph_key

# MCP 加密密钥
MCP_CREDENTIAL_ENCRYPTION_KEY=your_encryption_key

# 代理设置（如果需要）
HTTP_PROXY=http://your-proxy:port
HTTPS_PROXY=http://your-proxy:port
NO_PROXY=localhost,127.0.0.1
```

#### 2. 前端配置 (`frontend/.env.local`)

创建 `frontend/.env.local` 文件：

```bash
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key

# 其他前端配置
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 常见个人配置

### 代理配置

如果你在公司网络或需要使用代理，在 `backend/.env` 中添加：

```bash
HTTP_PROXY=http://proxy.company.com:8080
HTTPS_PROXY=http://proxy.company.com:8080
NO_PROXY=localhost,127.0.0.1,.local
```

### 默认模型选择

在 `backend/.env` 中配置：

```bash
# 设置默认使用的 LLM 提供商和模型
DEFAULT_LLM_PROVIDER=anthropic
DEFAULT_MODEL=claude-3-5-sonnet-20241022
```

### Redis 配置

如果使用远程 Redis：

```bash
REDIS_HOST=your_redis_host
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
```

## 代码修改记录

为了支持个人配置，以下文件已被修改（同步上游时需要注意冲突）：

### 1. `backend/core/ai_models/registry.py`

**修改原因**：添加 Gemini 模型支持

**修改内容**：
- 启用了 `Gemini 2.0 Flash` 模型（line ~210）
- 启用了 `Gemini 2.5 Pro` 模型（line ~231）

**同步时处理**：
- 如果上游修改了模型列表，需要手动合并
- 确保 Gemini 模型注册代码保留
- 或者重新添加你需要的模型

**备选方案**：
如果经常遇到冲突，可以考虑：
1. Fork 一个独立的模型配置分支
2. 或者在 `backend/.env` 中设置 `DEFAULT_MODEL=gemini/gemini-2.0-flash-exp`

## 同步上游更新

现在你基于 `upstream/main` 工作，同步更新相对简单：

```bash
# 获取上游更新
git fetch upstream

# 合并到本地（可能有冲突）
git pull upstream main

# 检查冲突文件
git status

# 如果有冲突，手动解决后：
git add .
git commit -m "merge: resolve conflicts with upstream"

# 推送到你的远程仓库
git push origin main
```

或者使用 Cursor 命令：`/check-upstream`

### 处理合并冲突

如果 `backend/core/ai_models/registry.py` 有冲突：

1. 打开文件，找到冲突标记 `<<<<<<<`, `=======`, `>>>>>>>`
2. 保留你的 Gemini 模型注册代码
3. 合并上游的其他模型更新
4. 删除冲突标记
5. 测试确保模型列表正常显示

## 安全最佳实践

1. **永远不要提交 `.env` 文件**：这些文件包含敏感信息
2. **使用强密码和密钥**：特别是数据库和加密密钥
3. **定期轮换密钥**：特别是 API 密钥和访问令牌
4. **不要在代码中硬编码密钥**：始终使用环境变量
5. **备份你的配置**：但要安全地存储（使用密码管理器）

## 故障排除

### 问题：环境变量未加载

确保：
- 配置文件名正确（`.env` 不是 `.env.txt`）
- 配置文件在正确的目录下
- 重启开发服务器以加载新配置

### 问题：代理设置不生效

尝试：
- 检查代理地址和端口是否正确
- 确保 `NO_PROXY` 包含 localhost
- 某些工具可能需要大写的环境变量名（`HTTP_PROXY` vs `http_proxy`）

## 参考

- [项目 README](README.md)
- [贡献指南](CONTRIBUTING.md)
- [Supabase 文档](https://supabase.com/docs)
- [Daytona 文档](https://daytona.io/docs)

## 获取帮助

- [Discord 社区](https://discord.gg/RvFhXUdZ9H)
- [GitHub Issues](https://github.com/kortix-ai/suna/issues)
- [Twitter](https://x.com/kortixai)

