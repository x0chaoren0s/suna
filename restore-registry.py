#!/usr/bin/env python3
"""
恢复 backend/core/ai_models/registry.py 文件
从备份中恢复个人修改
"""
import sys
from pathlib import Path

REGISTRY_FILE = Path("backend/core/ai_models/registry.py")
BACKUP_DIR = Path(".registry-backups")
LATEST_BACKUP = BACKUP_DIR / "registry.py.backup.latest"

def list_backups():
    """列出所有可用的备份"""
    backups = sorted(BACKUP_DIR.glob("registry.py.backup.*"), reverse=True)
    backups = [b for b in backups if b.is_file() and not b.name.endswith('.latest')]
    return backups

def main():
    if not BACKUP_DIR.exists():
        print(f"[ERROR] 错误: 备份目录不存在 {BACKUP_DIR}")
        print("[TIP] 提示: 请先运行 backup-registry.py 创建备份")
        return 1
    
    backups = list_backups()
    
    if not backups:
        print(f"[ERROR] 错误: 没有找到备份文件")
        return 1
    
    # 如果指定了备份文件，使用指定的；否则使用最新的
    if len(sys.argv) > 1:
        backup_name = sys.argv[1]
        backup_file = BACKUP_DIR / backup_name
        if not backup_file.exists():
            print(f"[ERROR] 错误: 备份文件不存在 {backup_file}")
            print("\n可用的备份:")
            for i, b in enumerate(backups[:10], 1):
                print(f"  {i}. {b.name}")
            return 1
    else:
        # 使用最新的备份
        if LATEST_BACKUP.exists():
            if LATEST_BACKUP.is_symlink():
                backup_file = BACKUP_DIR / LATEST_BACKUP.readlink()
            else:
                # 读取文本文件中的备份文件名
                backup_name = LATEST_BACKUP.read_text().strip()
                backup_file = BACKUP_DIR / backup_name
                if not backup_file.exists():
                    backup_file = backups[0]
        else:
            backup_file = backups[0]
    
    # 备份当前文件（以防万一）
    if REGISTRY_FILE.exists():
        current_backup = BACKUP_DIR / f"registry.py.current.{backup_file.stem.split('.')[-1]}"
        import shutil
        shutil.copy2(REGISTRY_FILE, current_backup)
        print(f"[SAVE] 已保存当前文件到: {current_backup.name}")
    
    # 恢复备份
    import shutil
    shutil.copy2(backup_file, REGISTRY_FILE)
    
    print(f"[OK] 已恢复: {backup_file.name} -> {REGISTRY_FILE}")
    print(f"[INFO] 恢复的文件: {REGISTRY_FILE.absolute()}")
    
    if len(backups) > 1:
        print("\n其他可用备份:")
        for i, b in enumerate(backups[1:6], 2):  # 显示前5个
            print(f"  {i}. {b.name}")
        print(f"\n[TIP] 提示: 使用 'python restore-registry.py <备份文件名>' 恢复特定备份")
    
    return 0

if __name__ == "__main__":
    exit(main())

