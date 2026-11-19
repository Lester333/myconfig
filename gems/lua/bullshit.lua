local p = io.popen("ls -A /home/stock/gems")

for name in p:lines() do
    print(name)
end

p:close()
