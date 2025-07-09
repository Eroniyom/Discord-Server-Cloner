# Discord Server Cloner - The Eroniyom

## Installation

### Requirements
- Python 3.8+
- pip
- Discord account with permissions to manage the target servers

### Setup
1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install discord.py colorama psutil
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## What Does It Copy?
- **Roles** (except @everyone)
- **Channels** (text and voice)
- **Categories**
- **Emojis**
- **Server icon and name**

## What Does It NOT Copy?
- **Members** (users are not moved or invited)
- **Messages** (chat history is not cloned)
- **Server boosts**
- **Bans, invites, integrations, or webhooks**
- **Permissions for @everyone** (may need manual adjustment)

---

**Note:** You must have the necessary permissions on both the source and target servers to perform cloning actions.

