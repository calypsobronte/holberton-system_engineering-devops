# 0x06. Regular expression

```bash
calypsobronte@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
calypsobronte@ubuntu$
calypsobronte@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
calypsobronte@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
calypsobronte@ubuntu$ ./example.rb 127.0.0.a
```


