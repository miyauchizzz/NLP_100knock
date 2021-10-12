from string import Template

def temp(x, y, z):
    str1 = Template("$X 時の $Y は $Z")
    result = str1.substitute(X=x, Y=y, Z=z)
    return result

def main():
    x = input("x:")
    y = input("y:")
    z = input("z:")
    
    result = temp(x, y, z)
    print(result)

if __name__ == "__main__":
    main()
