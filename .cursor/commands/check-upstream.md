检查并同步上游仓库更新。执行以下步骤：

1. **备份个人修改**：
   - 在同步前，先运行 `python backup-registry.py` 备份 `backend/core/ai_models/registry.py`
   - 如果备份失败，提示用户并询问是否继续

2. 检查是否配置了 upstream 远程仓库（kortix-ai/suna），如果没有则添加

3. 获取上游仓库的最新更新（git fetch upstream）

4. 检查当前分支与 upstream/main 的关系

5. 显示上游有多少新提交

6. 显示最新的 5 个上游提交

7. 显示本地分支独有的提交

8. 询问用户是否要合并上游更新到当前分支

9. **如果用户同意合并**：
   - 执行合并操作（git merge upstream/main）
   - 合并完成后，检查 `backend/core/ai_models/registry.py` 是否被上游修改：
     - 使用 `git diff HEAD~1 HEAD -- backend/core/ai_models/registry.py` 检查合并提交中的更改
     - 或者使用 `git log --oneline --follow -- backend/core/ai_models/registry.py` 查看该文件的历史
     - 如果上游修改了这个文件，需要：
       a. 通知用户上游修改了 registry.py
       b. 检查是否有冲突
       c. 如果有冲突，提示用户：
          - 冲突位置和内容
          - 建议保留你的 Gemini 模型注册代码
          - 提供恢复备份的命令：`python restore-registry.py`
          - 或者手动合并冲突
       d. 如果没有冲突但文件被修改：
          - 提示用户检查上游的修改
          - 建议运行 `git diff HEAD~1 HEAD -- backend/core/ai_models/registry.py` 查看具体更改
          - 提醒用户可能需要重新添加 Gemini 模型配置
          - 提供恢复备份的命令作为参考

10. 如果合并成功且 registry.py 未被修改或已处理，显示合并后的提交历史并提醒用户推送

11. 如果合并时发生冲突，提供解决冲突的指导

注意事项：
- 如果分支与上游没有共同祖先，提醒用户并询问是否继续
- 使用清晰的中文提示信息
- 备份文件保存在 `.registry-backups/` 目录
- 如果上游修改了 registry.py，优先考虑保留用户的模型配置
