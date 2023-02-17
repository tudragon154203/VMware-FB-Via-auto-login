# Tool Tự Log Via FB qua VMWare - VMware FB Via Auto Login

*Author: Tú Dragon - group support Ngô Thành*

## Giới thiệu

Tool tự động bật/tắt máy ảo, nuôi via Facebook

Hãy tham gia group support Ngô Thành để xem video hướng dẫn sử dụng cụ thể

## Cài đặt

### Yêu cầu

1. Hệ điều hành: Windows, Linux (Ubuntu, Fedora,...). Không hỗ trợ MacOS
2. Đã cài VMWorkStation Pro với ít nhất 1 virtual machine
3. Đã cài python, chạy được *python3* trong command line/terminal
4. Đã thêm thư mục chứa "vmrun.exe" vào $PATH.
   * Đường dẫn windows mặc định: C:\Program Files (x86)\VMware\VMware Workstation
   * Linux: đã tự thêm vào $PATH khi cài đặt
   * Cách check: chạy *vmrun* trên command line/terminal, thấy không báo lỗi là OK.

Sau khi thỏa mãn các yêu cầu trên, download source code của repository này về tiến hành chạy tool thử như sau:

### Chinh file src/backend/config.json
Dung chung cho Linux va Windows, chi khac o duong dan file, thu muc

   * vm_root_dir: thư mục gốc chứa các virtual machines (VMs). Ex: "D:\VMware machines", "~/virtual machines"
   * log_path: đường dẫn file text sẽ ghi log vào. P.mềm tự tạo nếu chưa có. Ex: "..\..\log.txt", "../../log.txt"
   * keyword: cụm từ tìm kiếm. Tool sẽ chỉ khởi động những VMs có chứa cụm này trong trên. Ex: "via", "ads", "2023",...
   * (Optional) t_running: thời gian (tính theo giây) từ lúc bật đến lúc tắt 1 VM. Nên đủ để VM khởi động vào log vào Facebook, mặc định 60s. Nếu máy tính bạn quá chậm nên tăng thêm
   * (Optional) t_between_sessions: thời gian (tính theo giây) từ lúc tắt VM này đến lúc bật VM tiếp theo. Mặc định 3s.

   Cac muc config "screenshot" va "credentials" la tuy chon. Neu khong kich hoat screenshot (enable:false trong config.json) thi khong can quan tam credentials

### Khoi Chay
#### Windows

1. Mở command line, vào thư mục *src/backend:*

   ```
   cd /d "VMware FB Via auto login\src\backend"
   ```
2. Chỉnh sửa file config.json trong thư mục backend:

   Theo huong dan ben tren
   
3. Quay lại command line, khởi động phần mềm:

   ```
   python3 main.py
   ```

   Khi cửa sổ VMware Workstation hiện lên và bắt đầu chạy lần lượt các VMs, bạn đã khởi động thành công

#### Linux (Ubuntu, Fedora,...)

1. Mở terminal, vào thư mục *src/backend:*

   ```
   cd "VMware FB Via auto login/src/backend"
   ```
2. Chỉnh sửa file config.json trong thư mục backend:

   Theo huong dan ben tren

   
3. Quay lại terminal, khởi động phần mềm:

   ```
   python3 main.py
   ```

   Khi cửa sổ VMware Workstation hiện lên và bắt đầu chạy lần lượt các VMs, bạn đã khởi động thành công.
   Nếu cửa sổ VMware Workstation không hiện, hãy thử edit lại file bash ./run.sh. Sau khi sửa dòng đường dẫn trước dòng vmware &, hãy vào terminal và chạy:

   ```
   ./run.sh
   ```

## Cơ chế hoạt động

Tool này sử dụng command "vmrun", chỉ có trong các bản VMware Workstation Pro trở lên ở linux và windows.

Tool sẽ quét các file .vmx có chứa keyword bạn điều chỉnh trong vm_root_dir, sau đó sử dụng "vmrun start", "vmrun stop" để khởi động và tắt các máy ảo tìm được

Trong quá trình chạy, VMMonitor sẽ check xem máy ảo đã lên chưa. Trong tương lai sẽ phát triển tính năng chụp lại ảnh màn hình mỗi n ngày để người dùng check lại xem các con via có đang log in bình thường không.

## Dành cho Dev

Các bạn dev có thể fork repo này, hoặc tạo pull request nếu muốn đóng góp xây dựng tool hoàn thiện hơn.

License: GPL-3.0 license, được tái sử dụng thoải mái cho mọi mục đích.

Giải thích các lớp (class) mình đã để trong file "./Classes Diagram.md", và các phần code đã được comment khá đầy đủ

Phần frontend mình dự kiến sẽ sử dụng QML. IDE sử dụng để phát triển frontend sẽ là Qt Creator (bản Community), bạn nào có kinh nghiệm về phần này có thể liên hệ với mình nhé:

Email: minhtudragon1997@gmail.com

Facebook: https://www.facebook.com/minhtudragon
