# factorial.jl

# Function to calculate factorial
function factorial(n::Int)
    if n == 0
        return 1
    else
        return n * factorial(n - 1)
    end
end

# Main script
n = 10  # You can change this value to calculate factorial of a different number
println("The factorial of $n is ", factorial(n))
