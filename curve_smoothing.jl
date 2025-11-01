using Plots

list = zeros(50)
mid = div(length(list),2)
len = length(list)
list[len] = 1
list[1] = 2


new_list = []
x_axis = []

for i in range(1,length(list))
    push!(x_axis,i)
end

p = plot(x_axis,list, legend = false)

for j in range(1,100)
    for i in range(1,length(list)-1)
        
        if list[i]< list[i+1]
            push!(new_list,((list[i]+list[i+1])/2))
            list[i] = ((list[i]+list[i+1])/2)
            list[i+1] = ((list[i]+list[i+1])/2)*0.95
        end
        

    end
    for i in range(1,length(list)-2)
        if list[length(list)-i]< list[length(list)-i-1]
                push!(new_list,((list[length(list)-i]+list[length(list)-i-1])/2))
                list[length(list)-i] = ((list[length(list)-i]+list[length(list)-i-1])/2)
                list[length(list)-i-1] = ((list[length(list)-i]+list[length(list)-i-1])/2)*0.95
            
        end
    end
    println(list)
    plot!(x_axis, list, legend = false)
    display(p)
    sleep(0.05)
end










#print(new_list)

#print(length(list))
#print(length(new_list))
