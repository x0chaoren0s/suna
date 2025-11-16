#!/usr/bin/env python3
"""
备份 backend/core/ai_models/registry.py 文件
用于在同步上游更新前保存个人修改
"""
import os
import shutil
from datetime import datetime
from pathlib import Path

REGISTRY_FILE = Path("backend/core/ai_models/registry.py")
BACKUP_DIR = Path(".registry-backups")
BACKUP_FILE = BACKUP_DIR / f"registry.py.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"

def main():
    if not REGISTRY_FILE.exists():
        print(f"[ERROR] 错误: 文件不存在 {REGISTRY_FILE}")
        return 1
    
    # 创建备份目录
    BACKUP_DIR.mkdir(exist_ok=True)
    
    # 备份文件
    shutil.copy2(REGISTRY_FILE, BACKUP_FILE)
    
    # 创建最新备份的符号链接（方便恢复）
    latest_backup = BACKUP_DIR / "registry.py.backup.latest"
    if latest_backup.exists():
        latest_backup.unlink()
    try:
        latest_backup.symlink_to(BACKUP_FILE.name)
    except (OSError, NotImplementedError):
        # Windows 可能不支持符号链接，创建一个文本文件记录最新备份
        latest_backup.write_text(BACKUP_FILE.name)
    
    print(f"[OK] 已备份: {REGISTRY_FILE} -> {BACKUP_FILE}")
    print(f"[INFO] 备份位置: {BACKUP_FILE.absolute()}")
    
    # 清理旧备份（保留最近10个）
    backups = sorted(BACKUP_DIR.glob("registry.py.backup.*"), key=os.path.getmtime)
    if len(backups) > 10:
        for old_backup in backups[:-10]:
            if old_backup.is_file() and not old_backup.name.endswith('.latest'):
                old_backup.unlink()
                print(f"[DEL] 已删除旧备份: {old_backup.name}")
    
    return 0

if __name__ == "__main__":
    exit(main())

