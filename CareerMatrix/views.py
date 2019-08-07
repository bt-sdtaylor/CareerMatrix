from django.shortcuts import render
from CareerMatrix import models


def indexView(request):
    if "GET" == request.method:

        # get dropdown selections and categories and convert to list
        dropdown_raw = models.Role.objects.all()
        dropdown_list = list()
        for role in dropdown_raw:
            dropdown_list.append(role)

        categories_raw = models.Category.objects.all()
        categories_list = list()
        for category in categories_raw:
            categories_list.append(category.category)

        # assign to context
        context = {
            'dropdown': dropdown_list,
            'categories': categories_list,
            'data':'hide',
        }

        # render initial landing page on visit
        return render(request, 'index.html', context)
    else:
        
        # get the role selected
        role_selected = request.POST['roles']
        print(int(role_selected))

        curr_role_temp = int(role_selected)
        next_role_temp = curr_role_temp

        if curr_role_temp == 10:
            next_role_temp = 0
        elif curr_role_temp > 4:
            next_role_temp = curr_role_temp + 1
        elif curr_role_temp > 2:
            next_role_temp = 6
        elif curr_role_temp > 1:
            next_role_temp = 4
        else:
            next_role_temp = 5

        # get current and next role names
        curr_role = models.Role.objects.values('role').filter(pk = str(curr_role_temp))
        curr_role = curr_role[0]['role']

        print(curr_role)

        next_role = ''
        if next_role_temp:
            next_role = models.Role.objects.values('role').filter(pk = str(next_role_temp))
            next_role = next_role[0]['role']
            print(next_role)


        # add selected categories to list
        categories_selected = list()
        for i in range(10):
            temp = i + 1
            temp_var = 'access_chk' + str(temp)
            temp_val = request.POST.get(temp_var, False)

            if temp_val:
                categories_selected.append(int(temp_val))
        print(categories_selected)

        # get all categories
        categories_raw = models.Category.objects.all()
        categories_all = list()
        for category in categories_raw:
            categories_all.append(category.category)

        # get the relevant data from the database
        temp_dict = dict()

        # get year
        curr_year = ''
        next_year = ''
        for i in categories_selected:

            # current role year
            details_temp_curr = models.Detail.objects.values('year').filter(role_id = str(curr_role_temp), category_id = i)
            year_raw_curr = details_temp_curr[0]['year']
            year_curr = models.Year.objects.values('year').filter(pk = str(year_raw_curr))
            curr_year = year_curr[0]['year']
            
            print(curr_year)

            # next role year
            if next_role:
                details_temp_next = models.Detail.objects.values('year').filter(role_id = str(next_role_temp), category_id = i)
                year_raw_next = details_temp_next[0]['year']
                year_next = models.Year.objects.values('year').filter(pk = str(year_raw_next))
                next_year = year_next[0]['year']
                
                print(next_year)
            
            break

        # rearrange category names to adjust for display purposes
        counter = 0
        for i in categories_all:
            if (i == "Relationships - External"):
                categories_all[counter] = 'Relationships (External)'
            if (i == "Relationships - Internal"):
                categories_all[counter] = 'Relationships (Internal)'
            
            counter +=1


        for i in categories_selected:

            category_name = categories_all[i - 1]
            temp_dict[category_name] = dict()
            temp_dict[category_name]['Current Goals'] = dict()

            if (curr_role == 'Assistant Mgr.'):
                curr_role = 'Assistant Manager'
                temp_dict[category_name]['Current Goals']['role'] = curr_role
            else:
                temp_dict[category_name]['Current Goals']['role'] = curr_role

            temp_dict[category_name]['Current Goals']['year'] = curr_year

            if next_role:
                temp_dict[category_name]['Next Career Move'] = dict()

                if (next_role == 'Assistant Mgr.'):
                    next_role = 'Assistant Manager'
                    temp_dict[category_name]['Next Career Move']['role'] = next_role
                else:
                    temp_dict[category_name]['Next Career Move']['role'] = next_role

                temp_dict[category_name]['Next Career Move']['year'] = next_year
            
            # current year
            details_temp_curr = models.Detail.objects.values('billable_hours', 'general_content', 'sub_header_first_section', 'sub_content_first_section', 'sub_header_second_section', 'sub_content_second_section', 'sub_header_third_section', 'sub_content_third_section').filter(role_id = str(curr_role_temp), category_id = i)

            counter = 0
            try:
                bill_hours_curr = details_temp_curr[0]['billable_hours']
                temp_dict[category_name]['Current Goals']['bill_hours_curr'] = bill_hours_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try:
                general_content_curr = details_temp_curr[0]['general_content']
                temp_dict[category_name]['Current Goals']['general_content_curr'] = general_content_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try: 
                sub_header_first_curr = details_temp_curr[0]['sub_header_first_section']
                temp_dict[category_name]['Current Goals']['sub_header_first_curr'] = sub_header_first_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)
                    
            try:
                sub_content_first_curr = details_temp_curr[0]['sub_content_first_section']
                temp_dict[category_name]['Current Goals']['sub_content_first_curr'] = sub_content_first_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try:
                sub_header_second_curr = details_temp_curr[0]['sub_header_second_section']
                temp_dict[category_name]['Current Goals']['sub_header_second_curr'] = sub_header_second_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try:
                sub_content_second_curr = details_temp_curr[0]['sub_content_second_section']
                temp_dict[category_name]['Current Goals']['sub_content_second_curr'] = sub_content_second_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try: 
                sub_header_third_curr = details_temp_curr[0]['sub_header_third_section']
                temp_dict[category_name]['Current Goals']['sub_header_third_curr'] = sub_header_third_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            try:
                sub_content_third_curr = details_temp_curr[0]['sub_content_third_section']
                temp_dict[category_name]['Current Goals']['sub_content_third_curr'] = sub_content_third_curr
            except IndexError as ie:
                    counter += 1
                    print(ie)
            except Exception as e:
                    print(e)

            if (counter == 8):
                temp_dict[category_name]['Current Goals']['section_not_applicable'] = 'No goals for this stage.'


            # next year
            if next_role:
                details_temp_curr = models.Detail.objects.values('billable_hours', 'general_content', 'sub_header_first_section', 'sub_content_first_section', 'sub_header_second_section', 'sub_content_second_section', 'sub_header_third_section', 'sub_content_third_section').filter(role_id = str(next_role_temp), category_id = i)

                counter = 0
                try:
                    bill_hours_next = details_temp_curr[0]['billable_hours']
                    temp_dict[category_name]['Next Career Move']['bill_hours_next'] = bill_hours_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try: 
                    general_content_next = details_temp_curr[0]['general_content']
                    temp_dict[category_name]['Next Career Move']['general_content_next'] = general_content_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try: 
                    sub_header_first_next = details_temp_curr[0]['sub_header_first_section']
                    temp_dict[category_name]['Next Career Move']['sub_header_first_next'] = sub_header_first_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try:
                    sub_content_first_next = details_temp_curr[0]['sub_content_first_section']
                    temp_dict[category_name]['Next Career Move']['sub_content_first_next'] = sub_content_first_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try:
                    sub_header_second_next = details_temp_curr[0]['sub_header_second_section']
                    temp_dict[category_name]['Next Career Move']['sub_header_second_next'] = sub_header_second_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try:
                    sub_content_second_next = details_temp_curr[0]['sub_content_second_section']
                    temp_dict[category_name]['Next Career Move']['sub_content_second_next'] = sub_content_second_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try:
                    sub_header_third_next = details_temp_curr[0]['sub_header_third_section']
                    temp_dict[category_name]['Next Career Move']['sub_header_third_next'] = sub_header_third_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                try:
                    sub_content_third_next = details_temp_curr[0]['sub_content_third_section']
                    temp_dict[category_name]['Next Career Move']['sub_content_third_next'] = sub_content_third_next
                except IndexError as ie:
                    counter += 1
                    print(ie)
                except Exception as e:
                    print(e)

                if (counter == 8):
                    temp_dict[category_name]['Next Career Move']['section_not_applicable'] = 'No goals for this stage.'


        print(temp_dict)

        # assign to context
        context = {
            'role_selected': curr_role,
            'next_role': next_role,
            'curr_year': curr_year,
            'next_year': next_year,
            'display_data': temp_dict,
            'data':'show',
        }

        # render career paths, passing context formulated above
        return render(request, 'paths.html', context)

def pathView(request):
    if "GET" == request.method:
        return render(request, 'index.html', {"data":"show"})
    else:
        
        
        # need to pass through matpoltlib charts
        return render(request, 'index.html', {})
