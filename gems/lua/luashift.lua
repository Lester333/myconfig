
local function makeshift(arr)
    local result = {}

    while #arr > 0 do
        local min_index = 1

        for i = 2, #arr do
            if arr[i] < arr[min_index] then
                min_index = i
            end
        end

        table.insert(result, arr[min_index])
        table.remove(arr, min_index)
    end

    return result
end

local arr = {}

for i = 5000, 1, -1 do
    table.insert(arr, i)
end

local start = os.clock()
arr = makeshift(arr)
local finish = os.clock()

print(string.format("Lua: %.6f seconds", finish - start))

